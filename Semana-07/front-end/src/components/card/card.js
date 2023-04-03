import style from './card.module.css';
function Card({tipo, color, shadow, inputSetter, inputValue}){
    return(
        <div className={style.card} style={{backgroundColor: color}}>
            <div className={style.cardTitle}>
                <h1>Coordenada {tipo}</h1>
            </div>

            <div className={style.cardBody}>
                <p>Digite o valor da coordenada {tipo}</p>
                <input tipo="text" id={`coordenada ${tipo}`} name={`coordenada ${tipo}`} onChange={(e)=>inputSetter(Number(e.target.value))} value={inputValue} />
            </div>
        </div>
    );
}
export default Card;