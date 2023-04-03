import style from "./header.module.css";

function Header() {
  return (
    <div className={style.header}>
      <div className={style.dflex}>
        <div className={style.circle}></div>
        <h1 className={style.title}>Atividade Front-End Dobot</h1>
        <div className={style.circle}></div>
      </div>
    </div>
  );
}

export default Header;
