import React from "react";
import { Button as StyledButton } from "react-bootstrap";

const Button = ({ value }) => {
  return <StyledButton variant="outline-dark">{value}</StyledButton>;
};

export default Button;
