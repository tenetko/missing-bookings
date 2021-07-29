import { combineReducers } from "redux";
import { setOrderNumbersReducer, setSheetNumberReducer } from "./ProcessXlsxForm/reducers";

const reducers = {
    setOrderNumbers: setOrderNumbersReducer,
    setSheetNumber: setSheetNumberReducer
};

const rootReducer = combineReducers(reducers);

export type RootState = ReturnType<typeof rootReducer>
export default rootReducer;