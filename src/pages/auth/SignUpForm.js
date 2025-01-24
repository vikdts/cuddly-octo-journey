import React from "react";
import { Link } from "react-router-dom";
import { Col, Row, Container } from "react-bootstrap";

const SignUpForm = () => {
  return (
    <Row>
        <Col>
      <Container>
        <h1>sign up</h1>
      </Container>
      <Container>
        <Link>Have an account?</Link>
      </Container>
      </Col>
    </Row>
  );
};

export default SignUpForm;
