import React from "react";
import Button from "./Button";
import { ButtonGroup } from "react-bootstrap";

function Panel() {
  return (
    <div className="d-flex flex-column">
      <ButtonGroup size="lg">
        <Button value={1} />
        <Button value={2} />
        <Button value={3} />
        <Button value={"+"} />
      </ButtonGroup>
      <ButtonGroup size="lg">
        <Button value={4} />
        <Button value={5} />
        <Button value={6} />
        <Button value={"-"} />
      </ButtonGroup>
      <ButtonGroup size="lg">
        <Button value={7} />
        <Button value={8} />
        <Button value={9} />
        <Button value={0} />
      </ButtonGroup>
    </div>
  );
}

export default Panel;
