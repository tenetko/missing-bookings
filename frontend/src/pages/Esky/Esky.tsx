import React from 'react';
import { useDispatch } from "react-redux";
import ProcessXlsxForm from "../../components/ProcessXlsxForm";
import { setOrderNumbers, setSheetNumber, processXlsxForm } from "../../store/ProcessXlsxForm/actions";
import {Space, Typography} from 'antd';

const {Title} = Typography;

const Esky: React.FC = () => {
    const dispatch = useDispatch();

    const callbacks = {
        setOrderNumbers: (...args: Parameters<typeof setOrderNumbers>) => dispatch(setOrderNumbers(...args)),
        setSheetNumber: (...args: Parameters<typeof setSheetNumber>) => dispatch(setSheetNumber(...args)),
        processXlsxForm: (...args: Parameters<typeof processXlsxForm>) => dispatch(processXlsxForm(...args))
    }

    const apiEndpoint = "/esky/"

    return (
        <>
            <Space size="large" direction="vertical" align="center" style={{width: 700}}>
                <Title level={2}>eSky</Title>
                <ProcessXlsxForm
                    callbacks={callbacks}
                    apiEndpoint={apiEndpoint}
                />
            </Space>
        </>
    )
};

export default Esky;