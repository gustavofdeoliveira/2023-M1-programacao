// This file contains the functions to send and receive data from the backend
// Import axios to send requests to the backend
import axios from 'axios';

// Set the base path to an empty string
const basePath = "";

// Async function to send coordinates to the backend
export const sendCoordinates = async (x, y, z, r) => {
    // Use axios to send a POST request to the specified endpoint
    const response = await axios.post(basePath + '/coordinate/create', {
        coordinateX: x,
        coordinateY: y,
        coordinateZ: z,
        coordinateR: r,
    });
    // Return the data sent by the backend
    return response.data;
}

// Async function to get all coordinates from the backend
export const getCoordinates = async () => {
    // Use axios to send a GET request to the specified endpoint
    const response = await axios.get(basePath + '/coordinate/listAll');
    // Return the data sent by the backend
    return response.data;
}
