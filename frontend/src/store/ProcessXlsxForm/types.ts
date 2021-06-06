export type paramsSetOrderNumbers = Parameters<(orderNumbers: any) => void>;

export type paramsProcessXlsxForm = Parameters<({ formData }: {
    formData: FormData
    clientConfig: object
    onSuccess: any
    onError: any
    apiEndpoint: string
}) => void>;

export interface callPostResponse {
    data: string
    status: number
    request: XMLHttpRequest
}
