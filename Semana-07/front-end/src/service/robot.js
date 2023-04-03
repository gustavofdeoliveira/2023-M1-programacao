import axios from 'axios';

const basePath = "";

export const sendCoordinates = async (x, y, z, r) => {
    const response = await axios.post(basePath + '/coordinate/create', {
        coordinateX: x,
        coordinateY: y,
        coordinateZ: z,
        coordinateR: r,
    });
    return response.data;
}
export const getCoordinates = async () => {
    const response = await axios.get(basePath + '/coordinate/listAll');
    return response.data;
}