import React, { Component } from "react"

import axios from 'axios';
class About extends Component {


  state = {
    todos: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/emp/');
      const todos = await res.json();
      this.setState({
        todos
      });
    } catch (e) {
      console.log(e);
    }
  }


  
  render() {
    return (
        <div>
          
        {/* banner */}
        <div className="innerf-banner">
        </div>
        {/*//banner */}
        {/* Page details */}
        <div className="services-agile-breadcrumb">
          <div className="inner_breadcrumb">
            <ul className="short_ls">
              <li>
                <a href="index.html">Home</a>
                <span>| |</span>
              </li>
              <li>About</li>
            </ul>
          </div>
        </div>
        {/* //Page details */}
        {/*about-top*/}
        <div className="about-ftop-inn">
          <div className="container">
            <h3 className="tittlef-agileits-w3layouts">About Us</h3>
            <div className="abt-img">
              <h3 className="sub-w3ls-headf white-clrf">Shortly about Grounding Coaching Sessions.</h3>
            </div>
            
            
            <div className="abtf-info">
              <div className="about-grids">
                <h5>Why choose us</h5>
                <p className="paragraphf"><span className="fa fa-repeat" aria-hidden="true" /> 30+ Years of experience</p>
                <p className="paragraphf"><span className="fa fa-repeat" aria-hidden="true" /> Range of coaching</p>
                <p className="paragraphf"><span className="fa fa-repeat" aria-hidden="true" /> Books, DVD's, Podcasts</p>
                <p className="paragraphf"><span className="fa fa-repeat" aria-hidden="true" /> Pricing's Affordability</p>
              </div>
              <div className="about-grids">
                <h5>Coaching strategy sessions</h5>
                <p className="paragraphf">Vestibulum mi ligula, bibendum quis leo at, euismod cursus tortor. Etiam vulputate enim id est suscipit tincidunt. In
                  lectus lectus, euismod eu lacus non, blandit imperdiet nulla. </p>
              </div>
              <div className="about-grids">
                <h5>success coaching programs</h5>
                <p className="paragraphf">Curabitur posuere enim nec ante varius volutpat. Aenean ipsum elit, ultrices mollis purus quis, aliquet faucibus ex.
                  Aenean vel elementum lectus, sit amet euismod lorem.</p>
              </div>
            </div>

          

            <table class="table">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Email</th>
              <th scope="col">Mobile</th>
              <th scope="col">Position</th>
              <th scope="col">exprience</th>
              
            </tr>
          </thead>
          <tbody>

          {this.state.todos.map(item => (
            <tr>
              
              <td>{item.name}</td>
              <td>{item.email}</td>
              <td>{item.mobile}</td>
              <td>{item.position}</td>
              <td>{item.exprience}</td>


          </tr>
        ))}
          
      
          </tbody>
        </table>
          </div>
        </div>
        {/*//DRF API call */}

      
          
        <div className="stats-f">
          <div className="container">
            <h3 className="tittlef-agileits-w3layouts white-clrf">Things that make our coaching the best</h3>
            <div className="stats-f_inner_grids">
              <div className="col-md-6">
                <h3 className="sub-w3ls-headf white-clrf">30+ Years of experience</h3>
                <p className="paragraphf white-clrf ">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer quis tristique est, et egestas odio. Mauris ac tristique
                  arcu, interdum risus.Integer quis tristique.</p>
                <div className="stats-f_left counter_grid">
                  <span className="fa fa-book" aria-hidden="true" />
                  <p className="counter">145</p>
                  <h4>Courses</h4>
                </div>
                <div className="stats-f_left counter_grid1">
                  <span className="fa fa-users" aria-hidden="true" />
                  <p className="counter">365</p>
                  <h4>Happy clients</h4>
                </div>
              </div>
              <div className="col-md-6">
                <div className="stats-f_left counter_grid2">
                  <span className="fa fa-user-plus" aria-hidden="true" />
                  <p className="counter">563</p>
                  <h4>People loved</h4>
                </div>
                <div className="stats-f_left counter_grid3">
                  <span className="fa fa-trophy" aria-hidden="true" />
                  <p className="counter">1045</p>
                  <h4>Awards won</h4>
                </div>
                <h3 className="sub-w3ls-headf white-clrf">Success coaching programs</h3>
                <p className="paragraphf white-clrf ">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer quis tristique est, et egestas odio. Mauris ac tristique
                  arcu, interdum risus.Integer quis tristique.</p>
              </div>
              <div className="clearfix"> </div>
            </div>
          </div>
        </div>
        {/* //stats-f */}
        {/* about */}
        <div className="aboutf">
          <div className="container">
            <h3 className="tittlef-agileits-w3layouts">Top most popular courses</h3>
            <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer quis tristique est, et egestas odio. Mauris ac tristique
              arcu, sed interdum risus.Integer quis tristique est, et egestas odio. Mauris ac tristique arcu, sed interdum risus.</p>
          </div>
          <div className="banner_bottom_tab_grids">
            <div id="verticalTab" className="resp-vtabs" style={{display: 'block', width: '100%', margin: '0px'}}>
              <ul className="resp-tabs-list">
                <li className="resp-tab-item resp-tab-active" aria-controls="tab_item-0" role="tab">Courses</li>
                <li className="resp-tab-item" aria-controls="tab_item-1" role="tab">Marketing</li>
                <li className="resp-tab-item" aria-controls="tab_item-2" role="tab">Development</li>
                <li className="resp-tab-item" aria-controls="tab_item-3" role="tab">Business</li>
                <li className="resp-tab-item" aria-controls="tab_item-4" role="tab">Maths</li>
              </ul>
              <div className="resp-tabs-container">
                {/* tab1 */}
                <div className="resp-tab-content resp-tab-content-active" style={{display: 'block'}} aria-labelledby="tab_item-0">
                  {/* tabs-info */}
                  <div className="main-topicsf">
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bbf1.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="courses.html" className="buttonf">Know More</a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">IT Management</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bbf2.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="courses.html" className="buttonf">Know More</a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Core IT Skills</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bbf3.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="courses.html" className="buttonf">Know More</a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Databases</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bbf4.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="courses.html" className="buttonf">Know More</a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Mobile Apps</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="clearfix"> </div>
                  </div>
                  {/* //tabs-info */}
                  {/* tabs-info */}
                  <div className="main-topicsf">
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf1.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="#small-dialog" className="popup-with-zoom-anim buttonf"><span className="fa fa-play-circle-o" aria-hidden="true" /></a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Network And Security</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf2.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="#small-dialog" className="popup-with-zoom-anim buttonf"><span className="fa fa-play-circle-o" aria-hidden="true" /></a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Data Science</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf3.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="#small-dialog" className="popup-with-zoom-anim buttonf"><span className="fa fa-play-circle-o" aria-hidden="true" /></a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Game Development</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf4.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="#small-dialog" className="popup-with-zoom-anim buttonf"><span className="fa fa-play-circle-o" aria-hidden="true" /></a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Hardware</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="clearfix"> </div>
                    {/* // video-button-popup */}
                    <div id="small-dialog" className="mfp-hide">
                      <iframe src="https://player.vimeo.com/video/7273286" />
                    </div>
                    {/* // video-button-popup */}
                  </div>
                  {/* //tabs-info */}
                </div>
                {/* //tab1 */}
                {/* tab2 */}
                <div className="resp-tab-content" aria-labelledby="tab_item-1">
                  {/* tabs-info */}
                  <div className="main-topicsf">
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf5.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="marketing.html" className="buttonf">Know More</a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Digital marketing</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf2.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="marketing.html" className="buttonf">Know More</a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Marketing Management</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf6.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="marketing.html" className="buttonf">Know More</a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Social Media Marketing</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf7.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="marketing.html" className="buttonf">Know More</a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Public Relations</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="clearfix"> </div>
                  </div>
                  {/* //tabs-info */}
                  {/* tabs-info */}
                  <div className="main-topicsf">
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf4.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="#small-dialog1" className="popup-with-zoom-anim buttonf"><span className="fa fa-play-circle-o" aria-hidden="true" /></a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Social Media Marketing</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bbf2.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="#small-dialog1" className="popup-with-zoom-anim buttonf"><span className="fa fa-play-circle-o" aria-hidden="true" /></a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Digital marketing</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf1.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="#small-dialog1" className="popup-with-zoom-anim buttonf"><span className="fa fa-play-circle-o" aria-hidden="true" /></a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Public Relations</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf7.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="#small-dialog1" className="popup-with-zoom-anim buttonf"><span className="fa fa-play-circle-o" aria-hidden="true" /></a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Marketing Management</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="clearfix"> </div>
                    {/* // video-button-popup */}
                    <div id="small-dialog1" className="mfp-hide">
                      <iframe src="https://player.vimeo.com/video/55806355" />
                    </div>
                    {/* // video-button-popup */}
                  </div>
                  {/* //tabs-info */}
                </div>
                {/*// tab2 */}
                {/* tab3 */}
                <div className="resp-tab-content" aria-labelledby="tab_item-2">
                  {/* tabs-info */}
                  <div className="main-topicsf">
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bbf1.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="development.html" className="buttonf">Know More</a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Web Development</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bbf2.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="development.html" className="buttonf">Know More</a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Mobile Apps</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bbf3.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="development.html" className="buttonf">Know More</a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Programming Languages</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bbf4.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="development.html" className="buttonf">Know More</a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Game Development</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="clearfix"> </div>
                  </div>
                  {/* //tabs-info */}
                  {/* tabs-info */}
                  <div className="main-topicsf">
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf1.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="#small-dialog2" className="popup-with-zoom-anim buttonf"><span className="fa fa-play-circle-o" aria-hidden="true" /></a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Databases</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf2.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="#small-dialog2" className="popup-with-zoom-anim buttonf"><span className="fa fa-play-circle-o" aria-hidden="true" /></a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Software Testing</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf3.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="#small-dialog2" className="popup-with-zoom-anim buttonf"><span className="fa fa-play-circle-o" aria-hidden="true" /></a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Software Engineering</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf4.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="#small-dialog2" className="popup-with-zoom-anim buttonf"><span className="fa fa-play-circle-o" aria-hidden="true" /></a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Development Tools</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="clearfix"> </div>
                    {/* // video-button-popup */}
                    <div id="small-dialog2" className="mfp-hide">
                      <iframe src="https://player.vimeo.com/video/53755097" />
                    </div>
                    {/* // video-button-popup */}
                  </div>
                  {/* //tabs-info */}
                </div>
                {/*// tab3 */}
                {/* tab4 */}
                <div className="resp-tab-content" aria-labelledby="tab_item-3">
                  {/* tabs-info */}
                  <div className="main-topicsf">
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf1.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="business.html" className="buttonf">Know More</a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Business Law</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf2.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="business.html" className="buttonf">Know More</a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Project Management</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf3.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="business.html" className="buttonf">Know More</a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">E-Commerce</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf4.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="business.html" className="buttonf">Know More</a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Strategy</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="clearfix"> </div>
                  </div>
                  {/* //tabs-info */}
                  {/* tabs-info */}
                  <div className="main-topicsf">
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bbf1.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="#small-dialog3" className="popup-with-zoom-anim buttonf"><span className="fa fa-play-circle-o" aria-hidden="true" /></a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Communications</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bbf2.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="#small-dialog3" className="popup-with-zoom-anim buttonf"><span className="fa fa-play-circle-o" aria-hidden="true" /></a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Entrepreneurship</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bbf3.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="#small-dialog3" className="popup-with-zoom-anim buttonf"><span className="fa fa-play-circle-o" aria-hidden="true" /></a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Finance</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bbf4.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="#small-dialog3" className="popup-with-zoom-anim buttonf"><span className="fa fa-play-circle-o" aria-hidden="true" /></a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Leadership &amp; Management</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="clearfix"> </div>
                    {/* // video-button-popup */}
                    <div id="small-dialog3" className="mfp-hide">
                      <iframe src="https://player.vimeo.com/video/198096211" />
                    </div>
                    {/* // video-button-popup */}
                  </div>
                  {/* //tabs-info */}
                </div>
                {/*// tab4 */}
                {/* tab5 */}
                <div className="resp-tab-content" aria-labelledby="tab_item-4">
                  {/* tabs-info */}
                  <div className="main-topicsf">
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf9.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="maths.html" className="buttonf">Know More</a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Algebra</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bbf2.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="maths.html" className="buttonf">Know More</a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Calculus</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf8.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="maths.html" className="buttonf">Know More</a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Core maths skills</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf10.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="maths.html" className="buttonf">Know More</a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Geometry</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="clearfix"> </div>
                  </div>
                  {/* //tabs-info */}
                  {/* tabs-info */}
                  <div className="main-topicsf">
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf1.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="#small-dialog4" className="popup-with-zoom-anim buttonf"><span className="fa fa-play-circle-o" aria-hidden="true" /></a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Probability &amp; Statistics</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf2.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="#small-dialog4" className="popup-with-zoom-anim buttonf"><span className="fa fa-play-circle-o" aria-hidden="true" /></a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Geometry</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf4.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="#small-dialog4" className="popup-with-zoom-anim buttonf"><span className="fa fa-play-circle-o" aria-hidden="true" /></a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Test Taking Skills</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="col-md-3 col-sm-6 tabsf-w3-agileits-grids">
                      <img src="images/bf3.jpg" alt="" />
                      <div className="img-caption">
                        <div className="tabs-inn-info-agileits-w3layouts">
                          <a href="#small-dialog4" className="popup-with-zoom-anim buttonf"><span className="fa fa-play-circle-o" aria-hidden="true" /></a>
                        </div>
                      </div>
                      <h3 className="sub-w3ls-headf">Series and Sequences</h3>
                      <p className="paragraphf">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. Donec maximus odio nec odio</p>
                    </div>
                    <div className="clearfix"> </div>
                    {/* // video-button-popup */}
                    <div id="small-dialog4" className="mfp-hide">
                      <iframe src="https://player.vimeo.com/video/110807219?color=c9ff23&byline=0" />
                    </div>
                    {/* // video-button-popup */}
                  </div>
                  {/* //tabs-info */}
                </div>
                {/*// tab5 */}
              </div>
            </div>
          </div>
        </div>
        {/* //about*/}
        {/* instructors section */}
        <div className="finner_team">
          <h3 className="tittlef-agileits-w3layouts">Instructors</h3>
          <div className="col-md-6 teamf-left">
            <div className="col-xs-4 fteam_grid_info">
              <img src="images/tf1.jpg" alt=" " className="img-responsive" />
              <h3>Maria Lisa</h3>
              <p>Professor of Marketing</p>
              <div className="teamf_icons">
                <ul>
                  <li>
                    <a href="#">
                      <i className="fa fa-facebook" aria-hidden="true" />
                    </a>
                  </li>
                  <li>
                    <a href="#">
                      <i className="fa fa-twitter" aria-hidden="true" />
                    </a>
                  </li>
                  <li>
                    <a href="#">
                      <i className="fa fa-dribbble" aria-hidden="true" />
                    </a>
                  </li>
                </ul>
              </div>
            </div>
            <div className="col-xs-4 fteam_grid_info">
              <img src="images/tf2.jpg" alt=" " className="img-responsive" />
              <h3>Pippa Molly</h3>
              <p>Corporate Marketing</p>
              <div className="teamf_icons">
                <ul>
                  <li>
                    <a href="#">
                      <i className="fa fa-facebook" aria-hidden="true" />
                    </a>
                  </li>
                  <li>
                    <a href="#">
                      <i className="fa fa-twitter" aria-hidden="true" />
                    </a>
                  </li>
                  <li>
                    <a href="#">
                      <i className="fa fa-dribbble" aria-hidden="true" />
                    </a>
                  </li>
                </ul>
              </div>
            </div>
            <div className="col-xs-4 fteam_grid_info">
              <img src="images/tf3.jpg" alt=" " className="img-responsive" />
              <h3>Carol Jan</h3>
              <p>Reader in Marketing</p>
              <div className="teamf_icons">
                <ul>
                  <li>
                    <a href="#">
                      <i className="fa fa-facebook" aria-hidden="true" />
                    </a>
                  </li>
                  <li>
                    <a href="#">
                      <i className="fa fa-twitter" aria-hidden="true" />
                    </a>
                  </li>
                  <li>
                    <a href="#">
                      <i className="fa fa-dribbble" aria-hidden="true" />
                    </a>
                  </li>
                </ul>
              </div>
            </div>
            <div className="col-xs-4 fteam_grid_info">
              <img src="images/tf2.jpg" alt=" " className="img-responsive" />
              <h3>Adam Joe</h3>
              <p>Digital Marketing</p>
              <div className="teamf_icons">
                <ul>
                  <li>
                    <a href="#">
                      <i className="fa fa-facebook" aria-hidden="true" />
                    </a>
                  </li>
                  <li>
                    <a href="#">
                      <i className="fa fa-twitter" aria-hidden="true" />
                    </a>
                  </li>
                  <li>
                    <a href="#">
                      <i className="fa fa-dribbble" aria-hidden="true" />
                    </a>
                  </li>
                </ul>
              </div>
            </div>
            <div className="col-xs-4 fteam_grid_info">
              <img src="images/tf3.jpg" alt=" " className="img-responsive" />
              <h3>Neil Ryan</h3>
              <p>Director of Marketing</p>
              <div className="teamf_icons">
                <ul>
                  <li>
                    <a href="#">
                      <i className="fa fa-facebook" aria-hidden="true" />
                    </a>
                  </li>
                  <li>
                    <a href="#">
                      <i className="fa fa-twitter" aria-hidden="true" />
                    </a>
                  </li>
                  <li>
                    <a href="#">
                      <i className="fa fa-dribbble" aria-hidden="true" />
                    </a>
                  </li>
                </ul>
              </div>
            </div>
            <div className="col-xs-4 fteam_grid_info">
              <img src="images/tf1.jpg" alt=" " className="img-responsive" />
              <h3>Maria Lisa</h3>
              <p>Director of Marketing</p>
              <div className="teamf_icons">
                <ul>
                  <li>
                    <a href="#">
                      <i className="fa fa-facebook" aria-hidden="true" />
                    </a>
                  </li>
                  <li>
                    <a href="#">
                      <i className="fa fa-twitter" aria-hidden="true" />
                    </a>
                  </li>
                  <li>
                    <a href="#">
                      <i className="fa fa-dribbble" aria-hidden="true" />
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </div>
          <div className="col-md-6 teamf-right">
            <div className="date-text">
              <img src="images/tf1.jpg" alt=" " className="img-responsive" />
              <div className="clientf-info">
                <span className="fa fa-quote-left" aria-hidden="true" />
                <p>Pellentesque convallis diam consequat magna vulputate malesuada. Cras a ornare elit.</p>
                <h6>Maria Lisa</h6>
              </div>
              <div className="clearfix"> </div>
            </div>
            <div className="date-text text-right">
              <img src="images/tf2.jpg" alt=" " className="img-responsive" />
              <div className="clientf-info">
                <span className="fa fa-quote-left" aria-hidden="true" />
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. </p>
                <h6>Pippa Molly</h6>
              </div>
              <div className="clearfix"> </div>
            </div>
            <div className="date-text">
              <img src="images/tf3.jpg" alt=" " className="img-responsive" />
              <div className="clientf-info">
                <span className="fa fa-quote-left" aria-hidden="true" />
                <p>Pellentesque convallis diam consequat magna vulputate malesuada. Cras a ornare elit.</p>
                <h6>Carol Jan</h6>
              </div>
              <div className="clearfix"> </div>
            </div>
            <div className="date-text text-right">
              <img src="images/tf1.jpg" alt=" " className="img-responsive" />
              <div className="clientf-info">
                <span className="fa fa-quote-left" aria-hidden="true" />
                <p>Pellentesque convallis diam consequat magna vulputate malesuada. Cras a ornare elit.</p>
                <h6>Maria Lisa</h6>
              </div>
              <div className="clearfix"> </div>
            </div>
            <div className="date-text">
              <img src="images/tf2.jpg" alt=" " className="img-responsive" />
              <div className="clientf-info">
                <span className="fa fa-quote-left" aria-hidden="true" />
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. </p>
                <h6>Adam Joe</h6>
              </div>
              <div className="clearfix"> </div>
            </div>
            <div className="date-text text-right">
              <img src="images/tf3.jpg" alt=" " className="img-responsive" />
              <div className="clientf-info">
                <span className="fa fa-quote-left" aria-hidden="true" />
                <p>Pellentesque convallis diam consequat magna vulputate malesuada. Cras a ornare elit.</p>
                <h6>Neil Ryan</h6>
              </div>
              <div className="clearfix"> </div>
            </div>
          </div>
          <div className="clearfix"> </div>
        </div>
        
      </div>
    )
  }
}
export default About;