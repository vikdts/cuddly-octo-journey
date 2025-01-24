import React from "react";
import { Link } from "react-router-dom";

import styles from "../../styles/SignInUpForm.module.css";
import btnStyles from "../../styles/Button.module.css";
import appStyles from "../../App.module.css";

import { Col, Row, Container, Image } from "react-bootstrap";

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
      <Col>
        <Image />
      </Col>
    </Row>
  );
};

export default SignUpForm;
