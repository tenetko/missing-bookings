import axios from 'axios';

const url = 'http://localhost:8000/api/'

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