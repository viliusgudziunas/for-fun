import React, { useState } from "react";
import { FormGroup, FormLabel, FormControl, Button } from "react-bootstrap";
import "../styles/Login.css";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const validateForm = () => {
    return email.length > 0 && password.length > 0;
  };

  const handleEmailChange = event => {
    setEmail({
      email: event.target.value
    });
  };

  const handlePasswordChange = event => {
    setPassword({
      password: event.target.value
    });
  };

  const handleSubmit = event => {
    event.preventDefault();
  };

  return (
    <div className="Login">
      <form onSubmit={handleSubmit}>
        <FormGroup controlId="formBasicEmail">
          <FormLabel>Email</FormLabel>
          <FormControl
            autoFocus
            type="email"
            onChange={handleEmailChange}
            placeholder="Email"
          />
        </FormGroup>
        <FormGroup controlId="password">
          <FormLabel>Password</FormLabel>
          <FormControl
            onChange={handlePasswordChange}
            type="password"
            placeholder="Password"
          />
        </FormGroup>
        <Button block disabled={!validateForm} type="submit">
          Login
        </Button>
      </form>
    </div>
  );
}
