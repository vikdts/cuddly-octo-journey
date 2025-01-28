import axios from "axios";

axios.defaults.baseURL = 'https://cuddly-octo-journey-9a4868450ef0.herokuapp.com';
axios.defaults.headers.post['Content-Type'] = 'multipart/form-data';
axios.defaults.withCredentials = true;