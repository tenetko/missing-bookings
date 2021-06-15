import React from 'react';
import { useDispatch } from "react-redux";
import ProcessXlsxForm from "../../components/ProcessXlsxForm";
import { setOrderNumbers, processXlsxForm } from "../../store/ProcessXlsxForm/actions";
import {Space, Typography} from 'antd';

const {Title} = Typography;

const AirAstana: React.FC = () => {
    const dispatch = useDispatch();

    const callbacks = {
        setOrderNumbers: (...args: Parameters<typeof setOrderNumbers>) => dispatch(setOrderNumbers(...args)),
        processXlsxForm: (...args: Parameters<typeof processXlsxForm>) => dispatch(processXlsxForm(...args))
    }

    const apiEndpoint = "/airastana/"

    return (
        <>
            <Space size="large" direction="vertical" align="center" style={{width: 700}}>
                <Title level={2}>Air Astana</Title>
                <ProcessXlsxForm
                    callbacks={callbacks}
                    apiEndpoint={apiEndpoint}
                />
            </Space>
        </>
    )
};

export default AirAstana;