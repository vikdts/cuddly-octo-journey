import React from "react";
import { Link } from "react-router-dom";

import styles from "../../styles/SignInUpForm.module.css";
import btnStyles from "../../styles/Button.module.css";
import appStyles from "../../App.module.css";

import { Form, Button, Col, Row, Container, Image } from "react-bootstrap";

const SignUpForm = () => {
  return (
    <Row className={styles.Row}>
      <Col className="my-auto py-2 p-md-2" md={6}>
        <Container className={`${appStyles.Content} p-4 `}>
          <h1 className={styles.Header}>sign up</h1>
          <Form>
  <Form.Group controlId="formBasicEmail">
    <Form.Label>Email address</Form.Label>
    <Form.Control type="email" placeholder="Enter email" />
 
  </Form.Group>

  <Form.Group controlId="formBasicPassword">
    <Form.Label>Password</Form.Label>
    <Form.Control type="password" placeholder="Password" />
  </Form.Group>

  <Button variant="primary" type="submit">
    Submit
  </Button>
</Form>
        </Container>
        <Container className={`mt-3 ${appStyles.Content}`}>
          <Link className={styles.Link} to="/signin">
            Have an account? <span>SIGN IN</span>
          </Link>
        </Container>
      </Col>
      <Col
        className={`my-auto d-none d-md-block p-2 ${styles.SignUpCol}`}
        md={6}
      >
        <Image
          className={`${appStyles.FillerImage}`}
          src={
            "https://res.cloudinary.com/dmux1cvft/image/upload/v1737966869/pexels-ekaterina-bolovtsova-5264091_bjgzcm.jpg"
          }
        />
      </Col>
    </Row>
  );
};

export default SignUpForm;
