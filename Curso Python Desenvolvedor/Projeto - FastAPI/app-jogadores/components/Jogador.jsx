import React from "react";
import axios from "axios";

const Jogador = (props) => {
  const excluiJogador = (jogadorId) => {
    axios
      .delete(`http://localhost:8000/jogadores/${jogadorId}`)
      .then((response) => {
        console.log("Jogador excluído com sucesso: " + response.data);
      })
      .catch((error) => {
        console.error("There was an error deleting the jogador!", error);
      });
  };

  const editaJogador = (jogador) => {
    props.setJogadorId(jogador.id);
    props.setJogadorNome(jogador.nome);
    props.setJogadorIdade(jogador.idade);
    props.setJogadorTime(jogador.time);
    props.setTextoBotao('Atualizar');
  }

  return (
    <div>
      <p>
        <span className="fw-bold">
          {props.jogador.nome} - {props.jogador.idade} - {props.jogador.time}
        </span>
        <button
          onClick={() => editaJogador(props.jogador)}
          className="btn btn-sm"
        >
          <span className="badge rounded-pill bg-info">Editar</span>
        </button>
        <button
          onClick={() => excluiJogador(props.jogador.id)}
          className="btn btn-sm"
        >
          <span className="badge rounded-pill bg-danger">X</span>
        </button>
      </p>
    </div>
  );
};

export default Jogador;
