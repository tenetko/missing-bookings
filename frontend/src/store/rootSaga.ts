import { all, fork } from "redux-saga/effects";

import { watchProcessXlsxForm } from "./ProcessXlsxForm/sagas";

export default function* rootSaga() {
  yield all([
    fork(watchProcessXlsxForm)
  ]);
}