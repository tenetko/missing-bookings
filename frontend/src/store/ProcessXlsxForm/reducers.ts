import { Reducer } from 'redux';
import { ActionTypes } from './actions';

const orderNumbersInitialState = null

const setOrderNumbersReducer: Reducer = (state = orderNumbersInitialState, action) => {
    switch(action.type) {
        case ActionTypes.SET_ORDER_NUMBERS:
            const order_numbers = action.payload
            return order_numbers;

        default:
            return state;
    }
}

const sheetNumberInitialState = null

const setSheetNumberReducer: Reducer = (state = sheetNumberInitialState, action) => {
    switch(action.type) {
        case ActionTypes.SET_SHEET_NUMBER:
            const sheet_number = action.payload
            return sheet_number;
        default:
            return state;
    }
}

const processXlsxFormInitialState = undefined

const processXlsxFormReducer: Reducer = (state = processXlsxFormInitialState, action) => {
    switch(action.type) {
        case ActionTypes.PROCESS_XLSX_FORM_REQUEST:
            return processXlsxFormInitialState

        case ActionTypes.PROCESS_XLSX_FORM_FAILURE:
            return processXlsxFormInitialState

        case ActionTypes.PROCESS_XLSX_FORM_SUCCESS:
            const form_data = action.payload
            return form_data
    }
}

export { setOrderNumbersReducer, setSheetNumberReducer, processXlsxFormReducer }
