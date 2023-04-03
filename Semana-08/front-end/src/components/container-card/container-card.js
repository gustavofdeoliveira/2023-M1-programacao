import style from "./container-card.module.css";
import Card from "../card/card";
import { useState } from "react";
import { sendCoordinates } from "../../service/robot";

function CardContainer() {
  const [coordenadaX, setCoordenadaX] = useState(-1);
  const [coordenadaY, setCoordenadaY] = useState(-1);
  const [coordenadaZ, setCoordenadaZ] = useState(-1);
  const [coordenadaR, setCoordenadaR] = useState(-1);

  return (
    <div>
      <div className={style.containerCard}>
        <Card
          tipo={"X"}
          color={"#FA955A"}
          shadow={"#9A4D00"}
          inputSetter={setCoordenadaX}
          inputValue={coordenadaX}
        />
        <Card
          tipo={"Y"}
          color={"#FEBE4F"}
          shadow={"#9C4D00"}
          inputSetter={setCoordenadaY}
          inputValue={coordenadaY}
        />
        <Card
          tipo={"Z"}
          color={"#C9DCC2"}
          shadow={"#6f7f69"}
          inputSetter={setCoordenadaZ}
          inputValue={coordenadaZ}
        />
        <Card
          tipo={"R"}
          color={"#C9DCC2"}
          shadow={"#7F9D74"}
          inputSetter={setCoordenadaR}
          inputValue={coordenadaR}
        />
      </div>
      <div className={style.button}>
        <button
          onClick={async () => {
            await sendCoordinates(
              coordenadaX,
              coordenadaY,
              coordenadaZ,
              coordenadaR
            );
            window.location.reload();
          }}
        >
          Enviar coordenads
        </button>
      </div>
    </div>
  );
}
export default CardContainer;
