import { combineReducers } from "redux";
import { setOrderNumbersReducer } from "./ProcessXlsxForm/reducers";

const reducers = {
    setOrderNumbers: setOrderNumbersReducer
};

const rootReducer = combineReducers(reducers);

export type RootState = ReturnType<typeof rootReducer>
export default rootReducer;