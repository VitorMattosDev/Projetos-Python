//import { useState } from 'react'
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { useState, useEffect } from "react";
import axios from "axios";
import JogadorList from "/components/JogadorList";
import Jogador from "/components/Jogador";

function App() {
  const [jogadorList, setJogadorList] = useState([{}]);
  const [jogadorNome, setJogadorNome] = useState("");
  const [jogadorIdade, setJogadorIdade] = useState("");
  const [jogadorTime, setJogadorTime] = useState("");
  const [jogadorId, setJogadorId] = useState('');
  const [textoBotao, setTextoBotao] = useState('Cadastrar');

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/jogadores/")
      .then((response) => {
        console.log(response.data);
        setJogadorList(response.data);
      })
      .catch((error) => {
        console.error("There was an error fetching the jogadores!", error);
      });
  });

  const atualizaJogador = (jogador) => {
    axios.put(`http://localhost:8000/jogadores/${jogadorId}`, jogador)
      .then((response) => {
        console.log("Jogador atualizado com sucesso: " + response.data);
        // Limpar inputs após sucesso
        setJogadorNome("");
        setJogadorIdade("");
        setJogadorTime("");
        setJogadorId('');
        setTextoBotao('Cadastrar');
      })
      .catch((error) => {
        console.error("There was an error updating the jogador!", error);
      });
  }

  const adicionaJogador = (jogador) => {

    axios
      .post("http://localhost:8000/jogadores/", jogador)
      .then((response) => {
        console.log(response.data);
        // Limpar inputs após sucesso
        setJogadorNome("");
        setJogadorIdade("");
        setJogadorTime("");
      })
      .catch((error) => {
        console.error("There was an error adding the jogador!", error);
      });
  };

  const adicionaAtualizaJogador = () => {

      const idadeNum = parseInt(jogadorIdade, 10);
      const jogador = {
        jogador_nome: jogadorNome,
        jogador_idade: Number.isNaN(idadeNum) ? 0 : idadeNum,
        jogador_time: jogadorTime,
    };

    if (jogadorId) {
      atualizaJogador(jogador);
    } else{
      adicionaJogador(jogador);
    }
  }

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
                value={jogadorNome}
                onChange={(e) => setJogadorNome(e.target.value)}
                className="mb-2 form-control"
                placeholder="Informe o Nome"
              />
              <input
                type="number"
                value={jogadorIdade}
                onChange={(e) => setJogadorIdade(e.target.value)}
                className="mb-2 form-control"
                placeholder="Informe a Idade"
              />
              <input
                value={jogadorTime}
                onChange={(e) => setJogadorTime(e.target.value)}
                className="mb-2 form-control"
                placeholder="Informe o Time"
              />
              <button
                onClick={adicionaAtualizaJogador}
                className="btn btn-outline-success mb-4"
              >
                {textoBotao}
              </button>
            </span>
            <h5 className="card text-center text-white bg-dark mb-4 pb-1">
              Lista de jogadores
            </h5>
            <div>
              <JogadorList 
              jogadorList={jogadorList} 
              setJogadorId={setJogadorId}
              setJogadorNome={setJogadorNome}
              setJogadorIdade={setJogadorIdade}
              setJogadorTime={setJogadorTime}
              setTextoBotao={setTextoBotao}
              />
            </div>
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
