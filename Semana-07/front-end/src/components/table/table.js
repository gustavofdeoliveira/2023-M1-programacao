import style from "./table.module.css";
import { useEffect, useState } from "react";
import { getCoordinates } from "../../service/robot";

function Table() {
  const [coordenadas, setCoordenadas] = useState({ data: [] });
  useEffect(() => {
    getCoordinates().then((response) => {
      console.log(response);
      setCoordenadas(response);
    });
  }, []);
  return (
    <table className={style.table}>
      <thead>
        <tr>
          <th>Coordenada X</th>
          <th>Coordenada Y</th>
          <th>Coordenada Z</th>
          <th>Coordenada R</th>
        </tr>
      </thead>
      <tbody>
        {coordenadas.data.map((coordenada) => (
          <tr>
            <td>{coordenada.coordinateX}</td>
            <td>{coordenada.coordinateY}</td>
            <td>{coordenada.coordinateZ}</td>
            <td>{coordenada.coordinateR}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
export default Table;
