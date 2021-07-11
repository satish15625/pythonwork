import React from 'react';


import { Link } from 'react-router-dom';

function TopHeader(props) {
    return (
        <div className="header">
            <div className="header_topw3layouts_bar">
            <div className="container">
                <div className="header_agileits_left">
                <ul>
                    <li><i className="fa fa-phone" aria-hidden="true" /> +(+91) 70115855550</li>
                    <li><i className="fa fa-envelope-o" aria-hidden="true" /> <a href="mailto:info@example.com">info@example.com</a></li>
                </ul>
                </div>
                <div className="header_right">
                <a href="#" className="log" data-toggle="modal" data-target="#myModal">Login</a>
                </div>
                <div className="clearfix"> </div>
            </div>
            </div>
        
        
      <div className="modal video-modal fade" id="myModal" tabIndex={-1} role="dialog" aria-labelledby="myModal">
      <div className="modal-dialog" role="document">
        <div className="modal-content">
          <div className="modal-header">
            Sign In &amp; Sign Up
            <button type="button" className="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
          </div>
          <section>
            <div className="modal-body">
              <div className="loginf_module">
                <div className="module form-module">
                  <div className="toggle"><i className="fa fa-times fa-pencil" />
                    <div className="tooltip">Click Me</div>
                  </div>
                  <div className="form">
                    <h3>Login to your account</h3>
                    <form action="#" method="post">
                      <input type="text" name="Username" placeholder="Username" required />
                      <input type="password" name="Password" placeholder="Password" required />
                      <input type="submit" defaultValue="Login" />
                    </form>
                    <div className="cta"><a href="#">Forgot your password?</a></div>
                  </div>
                  <div className="form">
                    <h3>Create an account</h3>
                    <form action="#" method="post">
                      <input type="text" name="Username" placeholder="Username" required />
                      <input type="password" name="Password" placeholder="Password" required />
                      <input type="email" name="Email" placeholder="Email address" required />
                      <input type="text" name="Phone" placeholder="Phone Number" required />
                      <input type="submit" defaultValue="Register" />
                    </form>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>
      </div>
    </div>
    </div>
           
    );
}

export default TopHeader;