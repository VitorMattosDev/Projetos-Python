//import { useState } from 'react'
import "./App.css";

function App() {
  return (
    <>
      <div className="container">
        <div
          className="mt-3 justify-content-center align-items-center mx-auto"
          style={{ width: "60vw", backgroundColor: "#ffffff" }}
        >
          <h2 className="text-center text-white bg-success card mb-1">
            Gerenciamento de Jogadores
          </h2>
          <h6 className="card text-center text-white bg-success mb-1 pb-1">
            Informações de Jogador
          </h6>
          <div className="card-body text-center">
            <h5 className="card text-center text-white bg-dark mb-2 pb-1">
              Cadastro de jogadores
            </h5>
            <span className="card-text">
              <input
                className="mb-2 form-control"
                placeholder="Informe o Nome"
              />
              <input
                className="mb-2 form-control"
                placeholder="Informe a Idade"
              />
              <input
                className="mb-2 form-control"
                placeholder="Informe o Time"
              />
              <button className="btn btn-outline-success mb-4">
                Cadastrar
              </button>
            </span>
            <h5 className="card text-center text-white bg-dark mb-4 pb-1">
              Lista de jogadores
            </h5>
            <div></div>
          </div>
          <h6 className="card text-center text-light bg-success py-1">
            &copy; VM - 2025
          </h6>
        </div>
      </div>
    </>
  );
}

export default App;
