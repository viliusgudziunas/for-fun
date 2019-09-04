import React, { useState } from "react";
import { Button, FormGroup, FormControl, ControlLabel } from "react-bootstrap";

export const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const validateForm = () => {};

  return (
    <div>
      <label>
        <b>Email - {email}</b>
      </label>
      <br />
      <input type="text" placeholder="Enter Email" required />
      <br />
      <label>
        <b>Password - {password}</b>
      </label>
      <br />
      <input type="password" placeholder="Enter Password" required />
      <br />
      <button type="submit">Login</button>
    </div>
  );
};
