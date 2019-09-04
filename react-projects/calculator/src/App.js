import React from "react";
import "./App.css";
import Panel from "./components/Panel";
import ResultScreen from "./components/ResultScreen";

function App() {
  return (
    <div className="App">
      <ResultScreen className="result-screen" />
      <Panel />
    </div>
  );
}

export default App;
