import axios from 'axios';

const url = process.env.NODE_ENV === 'production'
    ? '/api/'
    : 'http://127.0.0.1:8080/api'

const httpClient = axios.create({
    baseURL: url,
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'HTTP_X_CSRFTOKEN',
    headers: {
        'Content-type': 'application/json',
    }
});

const validateStatus = (_: number): boolean => {
    return true
}

export const callPost = (url: string, data?: any, config: object = {}): object => {
    return httpClient.post(url, data, {...config, validateStatus})
}

export const callGet = (url: string) => {
    return httpClient.get(url)
}