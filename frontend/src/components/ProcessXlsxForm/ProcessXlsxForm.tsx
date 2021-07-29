import React from 'react';
import { useSelector } from 'react-redux';
import { Button, Descriptions, Divider, Input, InputNumber, message, Space, Upload } from 'antd';
import { RootState } from '../../store/rootReducer';
import { paramsSetOrderNumbers, paramsSetSheetNumber, paramsProcessXlsxForm } from '../../store/ProcessXlsxForm/types';

const { TextArea } = Input; 

interface Callbacks {
    setOrderNumbers: (...args: paramsSetOrderNumbers) => void,
    setSheetNumber: (...args: paramsSetSheetNumber) => void,
    processXlsxForm: (...args: paramsProcessXlsxForm) => void
}

interface Props {
    callbacks: Callbacks
    apiEndpoint: string
}

const ProcessXlsxForm: React.FC<Props> = (props) => {
    const { callbacks, apiEndpoint } = props
    const { setOrderNumbers, setSheetNumber, processXlsxForm } = callbacks

    const orderNumbersHandler = (data: any) => {
        const orderNumbers: string[] = data.target.value
            .split('\n')
            .filter((value: string) => value !== '')
            .map((value: string) => value.trim());

        setOrderNumbers({ orderNumbers })
    };

    const sheetNumberHandler = (data: any) => {
        const sheetNumber: string = data;

        setSheetNumber({ sheetNumber })
    };

    const draggerParams  = {
        name: 'file',
        accept: '.xlsx, .xls',
        multiple: false,
        // @ts-ignore
        customRequest({ file, onError, onProgress, onSuccess }) {
            const formData = new FormData();

            const sheet_number = sheetNumber == null
                ? 1
                : sheetNumber.sheetNumber;

            if (orderNumbers != null) {
                formData.append('order_numbers', orderNumbers.orderNumbers);
                formData.append('sheet_number', sheet_number);
                formData.append('file', file);

                const clientConfig = {
                    onUploadProgress: ({ total, loaded }: { total: number, loaded: number }) => {
                        onProgress({ percent: Number(Math.round(loaded / total * 100).toFixed(2)) })
                    }
                };
                
                processXlsxForm({ formData, clientConfig, onSuccess, onError, apiEndpoint })
            } else {
                message.error("The order numbers list should not be empty")
            }

        }
    };

    const orderNumbers = useSelector((state: RootState): any => state.setOrderNumbers)
    const sheetNumber = useSelector((state: RootState): any => state.setSheetNumber)

    return (
        <>
            <Space size="large" direction="horizontal" align="start">

                <Space size="small" direction="vertical" align="center">
                    <div>Order numbers:</div>
                        <TextArea
                            style={{ maxWidth: 400 }}
                            rows={ 10 }
                            onChange = { orderNumbersHandler }
                            allowClear
                        />
                    
                </Space>

                <Space size="small" direction="vertical" align="center">

                    <Space size="small" direction="horizontal" align="center">
                        <div>Sheet number (starting from 1):</div>
                        <InputNumber
                            defaultValue = {1}
                            onChange = { sheetNumberHandler } 
                    />
                    </Space>

                    <Space size="small" direction="vertical" align="center">
                        <Upload { ...draggerParams } >
                                <Button type="primary" size="large">
                                    <p className="ant-upload-text">Generate a CSV file for stats-admin</p>
                                </Button>
                        </Upload>
                    </Space>

                </Space>

            </Space>

            <Divider></Divider>
            <Space>
                <Descriptions title="Как этим пользоваться:" column={1}>
                    <Descriptions.Item>1. Загружаем список order_numbers, которых не хватает в нашей статистике, по одному order_number на строку.</Descriptions.Item>
                    <Descriptions.Item>2. Нажимаем “Generate a CSV file for stats admin.”</Descriptions.Item>
                    <Descriptions.Item>3. Загружаем XLSX-отчёт партнёра.</Descriptions.Item>
                    <Descriptions.Item>4. В ответ придёт CSV-файл для stats-admin.</Descriptions.Item>
                </Descriptions>
            </Space>
        </>
    )
};

export default ProcessXlsxForm;