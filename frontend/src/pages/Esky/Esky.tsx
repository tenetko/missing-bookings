import React from 'react';
import { useDispatch } from "react-redux";
import ProcessXlsxForm from "../../components/ProcessXlsxForm";
import { setOrderNumbers, processXlsxForm } from "../../store/ProcessXlsxForm/actions";

const Esky: React.FC = () => {
    const dispatch = useDispatch();

    const callbacks = {
        setOrderNumbers: (...args: Parameters<typeof setOrderNumbers>) => dispatch(setOrderNumbers(...args)),
        processXlsxForm: (...args: Parameters<typeof processXlsxForm>) => dispatch(processXlsxForm(...args))
    }

    const apiEndpoint = "/esky/"

    return (
        <>
            <ProcessXlsxForm
                callbacks={callbacks}
                apiEndpoint={apiEndpoint}
            />
        </>
    )
};

export default Esky;