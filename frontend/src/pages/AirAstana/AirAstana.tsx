import React from 'react';
import { useDispatch } from "react-redux";
import ProcessXlsxForm from "../../components/ProcessXlsxForm";
import { setOrderNumbers, processXlsxForm } from "../../store/ProcessXlsxForm/actions";

const AirAstana: React.FC = () => {
    const dispatch = useDispatch();

    const callbacks = {
        setOrderNumbers: (...args: Parameters<typeof setOrderNumbers>) => dispatch(setOrderNumbers(...args)),
        processXlsxForm: (...args: Parameters<typeof processXlsxForm>) => dispatch(processXlsxForm(...args))
    }

    const apiEndpoint = "/airastana/"

    return (
        <>
            <ProcessXlsxForm
                callbacks={callbacks}
                apiEndpoint={apiEndpoint}
            />
        </>
    )
};

export default AirAstana;