import { put, takeEvery } from 'redux-saga/effects';
import { callPost } from '../../http_client';
import { ActionTypes } from './actions';
import { processXlsxForm } from './actions';
import { callPostResponse } from './types';


function* processXlsxFormSaga(action: ReturnType<typeof processXlsxForm>) {
    const { onError, onSuccess, apiEndpoint } = action.payload
    try {
        const res: callPostResponse = yield callPost(`${apiEndpoint}`, action.payload.formData);
        if (res.status !== 200) {
            yield put({ type: ActionTypes.PROCESS_XLSX_FORM_FAILURE });
            onError(new Error("server error"))
        }
        const filename = (getFilename(res.request.getResponseHeader('Content-Disposition')));
        const link = document.createElement('a');
        link.href = window.URL.createObjectURL(new Blob([res.data]));
        link.setAttribute('download', filename || 'stats-admin.csv');
        document.body.appendChild(link);
        link.click();
        yield put({ type: ActionTypes.PROCESS_XLSX_FORM_SUCCESS, payload: res.data });
        onSuccess()
    } catch (e) {
        yield put({ type: ActionTypes.PROCESS_XLSX_FORM_FAILURE});
        onError(new Error("server error"))
    }
}

function* watchProcessXlsxForm() {
    yield takeEvery(ActionTypes.PROCESS_XLSX_FORM_REQUEST, processXlsxFormSaga);
}

export const getFilename = (header: string | null): string => {
    const regExp = 'filename[^;\\n=]*=(([\'"]).*?\\2|[^;\\n]*)'
    if (header !== null) {
        const match = header.match(regExp)
        if (match !== null) return match[1]
    }
    return "default"
}

export { watchProcessXlsxForm };