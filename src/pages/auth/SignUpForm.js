import React from "react";
import { Link } from "react-router-dom";
import { Container } from "react-bootstrap";

const SignUpForm = () => {
  return (
    <Row>
      <Container>
        <h1>sign up</h1>
      </Container>
      <Container>
        <Link>Have an account?</Link>
      </Container>
    </Row>
  );
};

export default SignUpForm;
