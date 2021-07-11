import React from 'react';

function Footer(props) {
    return (
        <div>
        <div className="wthree-subscribef-w3ls">
          <div className="container">
            <h3 className="tittlef-agileits-w3layouts white-clrf">Sign up for our Newsletter</h3>
            <p className="white-clrf">Recieve our latest news straight to your inbox</p>
            <div className="footer_w3layouts_gridf_right">
              <form action="#" method="post">
                <input type="email" name="Email" placeholder="Email address..." required />
                <input type="submit" defaultValue="Submit" />
              </form>
            </div>
          </div>
        </div>
        {/*// Subscribe */}
        {/* footer */}
        <div className="footer_agileinfo_topf">
          <div className="container">
            <div className="col-md-4 footer_w3layouts_gridf">
              <h2><a href="index.html">Grounding</a></h2>
              <p className="paragraphf">Providing best coaching at affordable prices.</p>
            </div>
            <div className="col-md-4 footer_w3layouts_gridf">
              <nav>
                <ul className="footer_w3layouts_gridf_list">
                  <li><span className="fa fa-angle-right" aria-hidden="true" />
                    <a href="courses.html">Courses</a>
                  </li>
                  <li><span className="fa fa-angle-right" aria-hidden="true" />
                    <a href="marketing.html">Marketing</a>
                  </li>
                  <li><span className="fa fa-angle-right" aria-hidden="true" />
                    <a href="development.html">Development</a>
                  </li>
                  <li><span className="fa fa-angle-right" aria-hidden="true" />
                    <a href="maths.html">Maths</a>
                  </li>
                </ul>
              </nav>
            </div>
            <div className="col-md-4 footer_w3layouts_gridf">
              <nav>
                <ul className="footer_w3layouts_gridf_list">
                  <li><span className="fa fa-angle-right" aria-hidden="true" />
                    <a href="business.html">Business</a>
                  </li>
                  <li><span className="fa fa-angle-right" aria-hidden="true" />
                    <a href="faq.html">Faq</a>
                  </li>
                  <li><span className="fa fa-angle-right" aria-hidden="true" />
                    <a href="tems.html">Terms &amp; Conditions</a>
                  </li>
                  <li><span className="fa fa-angle-right" aria-hidden="true" />
                    <a href="contact.html">Contact</a>
                  </li>
                </ul>
              </nav>
            </div>
            <div className="clearfix"> </div>
            <div className="w3ls-fsocial-grid">
              <h3 className="sub-w3ls-headf">Follow Us</h3>
              <div className="social-ficons">
                <ul>
                  <li><a href="#"><span className="fa fa-facebook" /> Facebook</a></li>
                  <li><a href="#"><span className="fa fa-twitter" /> Twitter</a></li>
                  <li><a href="#"><span className="fa fa-google" />Google</a></li>
                </ul>
              </div>
            </div>
          </div>
        </div>
        <div className="footer-wthree-copyf">
          <div className="container">
            <div className="addressf-agileits-w3layouts">
              <p><span className="fa fa-map-marker" aria-hidden="true" />Noida Mahagun Mywoods Gaur city .</p>
            </div>
            <p>© 2018 Grounding. All rights reserved | Design by <a href="http://www.codensity.in"> Codensity Developers</a></p>
            <div className="clearfix"> </div>
          </div>
        </div>
      </div>
    );
}

export default Footer;