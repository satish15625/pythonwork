import React from 'react';
import PropTypes from 'prop-types';
import { Helmet, HelmetProvider } from 'react-helmet-async';
import TopHeader from "../skillup/components/Header/TopHeader";
import MiddleHeader from "../skillup/components/Header/MiddleHeader";
import Nav from "../skillup/components/Header/Nav";
import Banner from "../skillup/components/Fullpage/Fullpage";
import Footer from "../skillup/components/Footer/Footer";




const Main = (props) => (
    <HelmetProvider>
    <TopHeader />
    <MiddleHeader />
    <Helmet titleTemplate="%s | skillup" defaultTitle="Skiilup" defer={false}>
      {props.title && <title>{props.title}</title>}
      <meta name="description" content={props.description} />
    </Helmet>
    <div id="wrapper">
      <Nav />
      <div id="main">
        {props.children}
      </div>
      {props.fullPage ? null : <Banner />}
    </div>
    <Footer />
  </HelmetProvider>
  );

  Main.propTypes = {
    children: PropTypes.oneOfType([
      PropTypes.arrayOf(PropTypes.node),
      PropTypes.node,
    ]),
    fullPage: PropTypes.bool,
    title: PropTypes.string,
    description: PropTypes.string,
  };
  
  Main.defaultProps = {
    children: null,
    fullPage: false,
    title: null,
    description: "Skillup Persona Website website.",
  };
  
  export default Main;