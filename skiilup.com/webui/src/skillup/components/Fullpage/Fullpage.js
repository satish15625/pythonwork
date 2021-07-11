import React from 'react';

function Banner(props) {
    return (
          
        <div id="myCarousel" className="carousel slide" data-ride="carousel">
            <ol className="carousel-indicators">
            <li data-target="#myCarousel" data-slide-to={0} className="active" />
            <li data-target="#myCarousel" data-slide-to={1} className />
            <li data-target="#myCarousel" data-slide-to={2} className />
            <li data-target="#myCarousel" data-slide-to={3} className />
            <li data-target="#myCarousel" data-slide-to={4} className />
            </ol>
            <div className="carousel-inner" role="listbox">
            <div className="item active">
                <div className="container">
                <div className="carousel-caption">
                    <p>Courses</p>
                    <h3>We provide best courses within the <span>shortest terms.</span></h3>
                </div>
                </div>
            </div>
            <div className="item item2">
                <div className="container">
                <div className="carousel-caption">
                    <p>Marketing</p>
                    <h3>Change your thoughts for a <span>better you.</span></h3>
                </div>
                </div>
            </div>
            <div className="item item3">
                <div className="container">
                <div className="carousel-caption">
                    <p>Development</p>
                    <h3>Simple ways to beat <span>procrastination.</span></h3>
                </div>
                </div>
            </div>
            <div className="item item4">
                <div className="container">
                <div className="carousel-caption">
                    <p>Business</p>
                    <h3>Modernizing, virtualizing your <span>business!</span></h3>
                </div>
                </div>
            </div>
            <div className="item item5">
                <div className="container">
                <div className="carousel-caption">
                    <p>Maths</p>
                    <h3>Achieve More with Grounding <span> Coaching Sessions.</span></h3>
                </div>
                </div>
            </div>
            </div>
            <a className="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
            <span className="fa fa-chevron-left" aria-hidden="true" />
            <span className="sr-only">Previous</span>
            </a>
            <a className="right carousel-control" href="#myCarousel" role="button" data-slide="next">
            <span className="fa fa-chevron-right" aria-hidden="true" />
            <span className="sr-only">Next</span>
            </a>

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
        <div className="materialsf-section">
            <div className="container">
            <h3 className="tittlef-agileits-w3layouts white-clrf">Popular study materials.</h3>
            <div className="carousel slide materialf-slider" id="myCarousel1">
                <div className="carousel-inner">
                <div className="item active">
                    <ul className="thumbnails">
                    <li className="col-md-3 col-sm-6 col-xs-6 mtrl-f-grids">
                        <div className="fff">
                        <div className="thumbnail">
                            <a href="shop_single.html"><img src="images/mf1.jpg" alt="" /></a>
                            <p><span className="fa fa-hand-o-down" aria-hidden="true" />Course Name</p>
                        </div>
                        <div className="caption">
                            <h4>Description About Study Material</h4>
                            <p>Clayton Barton</p>
                            <div className="matrlf-mid">
                            <h6><span>$</span> 100.00</h6>
                            <ul className="rating">
                                <li>
                                <a href="#">
                                    <span className="fa fa-star yellow-star" aria-hidden="true" />
                                </a>
                                </li>
                                <li>
                                <a href="#">
                                    <span className="fa fa-star yellow-star" aria-hidden="true" />
                                </a>
                                </li>
                                <li>
                                <a href="#">
                                    <span className="fa fa-star yellow-star" aria-hidden="true" />
                                </a>
                                </li>
                                <li>
                                <a href="#">
                                    <span className="fa fa-star yellow-star" aria-hidden="true" />
                                </a>
                                </li>
                                <li>
                                <a href="#">
                                    <span className="fa fa-star gray-star" aria-hidden="true" />
                                </a>
                                </li>
                            </ul>
                            <div className="clearfix"> </div>
                            </div>
                            <form action="#" method="post">
                            <input type="hidden" name="cmd" defaultValue="_cart" />
                            <input type="hidden" name="add" defaultValue={1} />
                            <input type="hidden" name="edu_item" defaultValue="Book1" />
                            <input type="hidden" name="amount" defaultValue={100.00} />
                            <button type="submit" className="edu-cart pedu-cart"><i className="fa fa-cart-plus" aria-hidden="true" /> Add to cart</button>
                            <a href="#" data-toggle="modal" data-target="#myModal1" />
                            </form>
                        </div>
                        </div>
                    </li>
                    <li className="col-md-3 col-sm-6 col-xs-6 mtrl-f-grids">
                        <div className="fff">
                        <div className="thumbnail">
                            <a href="shop_single.html"><img src="images/mf2.jpg" alt="" /></a>
                            <p><span className="fa fa-hand-o-down" aria-hidden="true" />Course Name</p>
                        </div>
                        <div className="caption">
                            <h4>Description About Study Material</h4>
                            <p>Niel Fontine</p>
                            <div className="matrlf-mid">
                            <h6><span>$</span> 80.00</h6>
                            <ul className="rating">
                                <li>
                                <a href="#">
                                    <span className="fa fa-star yellow-star" aria-hidden="true" />
                                </a>
                                </li>
                                <li>
                                <a href="#">
                                    <span className="fa fa-star yellow-star" aria-hidden="true" />
                                </a>
                                </li>
                                <li>
                                <a href="#">
                                    <span className="fa fa-star yellow-star" aria-hidden="true" />
                                </a>
                                </li>
                                <li>
                                <a href="#">
                                    <span className="fa fa-star yellow-star" aria-hidden="true" />
                                </a>
                                </li>
                                <li>
                                <a href="#">
                                    <span className="fa fa-star gray-star" aria-hidden="true" />
                                </a>
                                </li>
                            </ul>
                            <div className="clearfix"> </div>
                            </div>
                            <form action="#" method="post">
                            <input type="hidden" name="cmd" defaultValue="_cart" />
                            <input type="hidden" name="add" defaultValue={1} />
                            <input type="hidden" name="edu_item" defaultValue="Book2" />
                            <input type="hidden" name="amount" defaultValue={80.00} />
                            <button type="submit" className="edu-cart pedu-cart"><i className="fa fa-cart-plus" aria-hidden="true" /> Add to cart</button>
                            <a href="#" data-toggle="modal" data-target="#myModal1" />
                            </form>
                        </div>
                        </div>
                    </li>
                    <li className="col-md-3 col-sm-6 col-xs-6 mtrl-f-grids">
                        <div className="fff">
                        <div className="thumbnail">
                            <a href="shop_single.html"><img src="images/mf3.jpg" alt="" /></a>
                            <p><span className="fa fa-hand-o-down" aria-hidden="true" />Course Name</p>
                        </div>
                        <div className="caption">
                            <h4>Description About Study Material</h4>
                            <p>Jose portilla</p>
                            <div className="matrlf-mid">
                            <h6><span>$</span> 30.00</h6>
                            <ul className="rating">
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star gray-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star gray-star" aria-hidden="true" /></a></li>
                            </ul>
                            <div className="clearfix"> </div>
                            </div>
                            <form action="#" method="post">
                            <input type="hidden" name="cmd" defaultValue="_cart" />
                            <input type="hidden" name="add" defaultValue={1} />
                            <input type="hidden" name="edu_item" defaultValue="Book3" />
                            <input type="hidden" name="amount" defaultValue={30.00} />
                            <button type="submit" className="edu-cart pedu-cart"><i className="fa fa-cart-plus" aria-hidden="true" /> Add to cart</button>
                            <a href="#" data-toggle="modal" data-target="#myModal1" />
                            </form>
                        </div>
                        </div>
                    </li>
                    <li className="col-md-3 col-sm-6 col-xs-6 mtrl-f-grids">
                        <div className="fff">
                        <div className="thumbnail">
                            <a href="shop_single.html"><img src="images/mf4.jpg" alt="" /></a>
                            <p><span className="fa fa-hand-o-down" aria-hidden="true" />Course Name</p>
                        </div>
                        <div className="caption">
                            <h4>Description About Study Material</h4>
                            <p>Chris Haroun</p>
                            <div className="matrlf-mid">
                            <h6><span>$</span> 60.00</h6>
                            <ul className="rating">
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star gray-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star gray-star" aria-hidden="true" /></a></li>
                            </ul>
                            <div className="clearfix"> </div>
                            </div>
                            <form action="#" method="post">
                            <input type="hidden" name="cmd" defaultValue="_cart" />
                            <input type="hidden" name="add" defaultValue={1} />
                            <input type="hidden" name="edu_item" defaultValue="Book4" />
                            <input type="hidden" name="amount" defaultValue={60.00} />
                            <button type="submit" className="edu-cart pedu-cart"><i className="fa fa-cart-plus" aria-hidden="true" /> Add to cart</button>
                            <a href="#" data-toggle="modal" data-target="#myModal1" />
                            </form>
                        </div>
                        </div>
                    </li>
                    </ul>
                </div>
                {/* /Slide1 */}
                <div className="item">
                    <ul className="thumbnails">
                    <li className="col-md-3 col-sm-6 col-xs-6 mtrl-f-grids">
                        <div className="fff">
                        <div className="thumbnail">
                            <a href="shop_single.html"><img src="images/mf5.jpg" alt="" /></a>
                            <p><span className="fa fa-hand-o-down" aria-hidden="true" />Course Name</p>
                        </div>
                        <div className="caption">
                            <h4>Description About Study Material</h4>
                            <p>Alex Even</p>
                            <div className="matrlf-mid">
                            <h6><span>$</span> 80.00</h6>
                            <ul className="rating">
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                            </ul>
                            <div className="clearfix"> </div>
                            </div>
                            <form action="#" method="post">
                            <input type="hidden" name="cmd" defaultValue="_cart" />
                            <input type="hidden" name="add" defaultValue={1} />
                            <input type="hidden" name="edu_item" defaultValue="Book5" />
                            <input type="hidden" name="amount" defaultValue={80.00} />
                            <button type="submit" className="edu-cart pedu-cart"><i className="fa fa-cart-plus" aria-hidden="true" /> Add to cart</button>
                            <a href="#" data-toggle="modal" data-target="#myModal1" />
                            </form>
                        </div>
                        </div>
                    </li>
                    <li className="col-md-3 col-sm-6 col-xs-6 mtrl-f-grids">
                        <div className="fff">
                        <div className="thumbnail">
                            <a href="shop_single.html"><img src="images/mf6.jpg" alt="" /></a>
                            <p><span className="fa fa-hand-o-down" aria-hidden="true" />Course Name</p>
                        </div>
                        <div className="caption">
                            <h4>Description About Study Material</h4>
                            <p>Hadilen de</p>
                            <div className="matrlf-mid">
                            <h6><span>$</span> 60.00</h6>
                            <ul className="rating">
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star gray-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star gray-star" aria-hidden="true" /></a></li>
                            </ul>
                            <div className="clearfix"> </div>
                            </div>
                            <form action="#" method="post">
                            <input type="hidden" name="cmd" defaultValue="_cart" />
                            <input type="hidden" name="add" defaultValue={1} />
                            <input type="hidden" name="edu_item" defaultValue="Book6" />
                            <input type="hidden" name="amount" defaultValue={60.00} />
                            <button type="submit" className="edu-cart pedu-cart"><i className="fa fa-cart-plus" aria-hidden="true" /> Add to cart</button>
                            <a href="#" data-toggle="modal" data-target="#myModal1" />
                            </form>
                        </div>
                        </div>
                    </li>
                    <li className="col-md-3 col-sm-6 col-xs-6 mtrl-f-grids">
                        <div className="fff">
                        <div className="thumbnail">
                            <a href="shop_single.html"><img src="images/mf1.jpg" alt="" /></a>
                            <p><span className="fa fa-hand-o-down" aria-hidden="true" />Course Name</p>
                        </div>
                        <div className="caption">
                            <h4>Description About Study Material</h4>
                            <p>Clayton</p>
                            <div className="matrlf-mid">
                            <h6><span>$</span> 70.00</h6>
                            <ul className="rating">
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star gray-star" aria-hidden="true" /></a></li>
                            </ul>
                            <div className="clearfix"> </div>
                            </div>
                            <form action="#" method="post">
                            <input type="hidden" name="cmd" defaultValue="_cart" />
                            <input type="hidden" name="add" defaultValue={1} />
                            <input type="hidden" name="edu_item" defaultValue="Book7" />
                            <input type="hidden" name="amount" defaultValue={70.00} />
                            <button type="submit" className="edu-cart pedu-cart"><i className="fa fa-cart-plus" aria-hidden="true" /> Add to cart</button>
                            <a href="#" data-toggle="modal" data-target="#myModal1" />
                            </form>
                        </div>
                        </div>
                    </li>
                    <li className="col-md-3 col-sm-6 col-xs-6 mtrl-f-grids">
                        <div className="fff">
                        <div className="thumbnail">
                            <a href="shop_single.html"><img src="images/mf2.jpg" alt="" /></a>
                            <p><span className="fa fa-hand-o-down" aria-hidden="true" />Course Name</p>
                        </div>
                        <div className="caption">
                            <h4>Description About Study Material</h4>
                            <p>Scott Harris</p>
                            <div className="matrlf-mid">
                            <h6><span>$</span> 50.00</h6>
                            <ul className="rating">
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star gray-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star gray-star" aria-hidden="true" /></a></li>
                            </ul>
                            <div className="clearfix"> </div>
                            </div>
                            <form action="#" method="post">
                            <input type="hidden" name="cmd" defaultValue="_cart" />
                            <input type="hidden" name="add" defaultValue={1} />
                            <input type="hidden" name="edu_item" defaultValue="Book8" />
                            <input type="hidden" name="amount" defaultValue={50.00} />
                            <button type="submit" className="edu-cart pedu-cart"><i className="fa fa-cart-plus" aria-hidden="true" /> Add to cart</button>
                            <a href="#" data-toggle="modal" data-target="#myModal1" />
                            </form>
                        </div>
                        </div>
                    </li>
                    </ul>
                </div>
                {/* /Slide2 */}
                <div className="item">
                    <ul className="thumbnails">
                    <li className="col-md-3 col-sm-6 col-xs-6 mtrl-f-grids">
                        <div className="fff">
                        <div className="thumbnail">
                            <a href="shop_single.html"><img src="images/mf3.jpg" alt="" /></a>
                            <p><span className="fa fa-hand-o-down" aria-hidden="true" />Course Name</p>
                        </div>
                        <div className="caption">
                            <h4>Description About Study Material</h4>
                            <p>Cordebard</p>
                            <div className="matrlf-mid">
                            <h6><span>$</span> 90.00</h6>
                            <ul className="rating">
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                            </ul>
                            <div className="clearfix"> </div>
                            </div>
                            <form action="#" method="post">
                            <input type="hidden" name="cmd" defaultValue="_cart" />
                            <input type="hidden" name="add" defaultValue={1} />
                            <input type="hidden" name="edu_item" defaultValue="Book9" />
                            <input type="hidden" name="amount" defaultValue={90.00} />
                            <button type="submit" className="edu-cart pedu-cart"><i className="fa fa-cart-plus" aria-hidden="true" /> Add to cart</button>
                            <a href="#" data-toggle="modal" data-target="#myModal1" />
                            </form>
                        </div>
                        </div>
                    </li>
                    <li className="col-md-3 col-sm-6 col-xs-6 mtrl-f-grids">
                        <div className="fff">
                        <div className="thumbnail">
                            <a href="shop_single.html"><img src="images/mf4.jpg" alt="" /></a>
                            <p><span className="fa fa-hand-o-down" aria-hidden="true" />Course Name</p>
                        </div>
                        <div className="caption">
                            <h4>Description About Study Material</h4>
                            <p>Michael Doe</p>
                            <div className="matrlf-mid">
                            <h6><span>$</span> 80.00</h6>
                            <ul className="rating">
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star gray-star" aria-hidden="true" /></a></li>
                            </ul>
                            <div className="clearfix"> </div>
                            </div>
                            <form action="#" method="post">
                            <input type="hidden" name="cmd" defaultValue="_cart" />
                            <input type="hidden" name="add" defaultValue={1} />
                            <input type="hidden" name="edu_item" defaultValue="Book10" />
                            <input type="hidden" name="amount" defaultValue={80.00} />
                            <button type="submit" className="edu-cart pedu-cart"><i className="fa fa-cart-plus" aria-hidden="true" /> Add to cart</button>
                            <a href="#" data-toggle="modal" data-target="#myModal1" />
                            </form>
                        </div>
                        </div>
                    </li>
                    <li className="col-md-3 col-sm-6 col-xs-6 mtrl-f-grids">
                        <div className="fff">
                        <div className="thumbnail">
                            <a href="shop_single.html"><img src="images/mf5.jpg" alt="" /></a>
                            <p><span className="fa fa-hand-o-down" aria-hidden="true" />Course Name</p>
                        </div>
                        <div className="caption">
                            <h4>Description About Study Material</h4>
                            <p>De Ponteves</p>
                            <div className="matrlf-mid">
                            <h6><span>$</span> 50.00</h6>
                            <ul className="rating">
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star gray-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star gray-star" aria-hidden="true" /></a></li>
                            </ul>
                            <div className="clearfix"> </div>
                            </div>
                            <form action="#" method="post">
                            <input type="hidden" name="cmd" defaultValue="_cart" />
                            <input type="hidden" name="add" defaultValue={1} />
                            <input type="hidden" name="edu_item" defaultValue="Book11" />
                            <input type="hidden" name="amount" defaultValue={50.00} />
                            <button type="submit" className="edu-cart pedu-cart"><i className="fa fa-cart-plus" aria-hidden="true" /> Add to cart</button>
                            <a href="#" data-toggle="modal" data-target="#myModal1" />
                            </form>
                        </div>
                        </div>
                    </li>
                    <li className="col-md-3 col-sm-6 col-xs-6 mtrl-f-grids">
                        <div className="fff">
                        <div className="thumbnail">
                            <a href="shop_single.html"><img src="images/mf6.jpg" alt="" /></a>
                            <p><span className="fa fa-hand-o-down" aria-hidden="true" />Course Name</p>
                        </div>
                        <div className="caption">
                            <h4>Description About Study Material</h4>
                            <p>Jhon Chriss</p>
                            <div className="matrlf-mid">
                            <h6><span>$</span> 70.00</h6>
                            <ul className="rating">
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star yellow-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star gray-star" aria-hidden="true" /></a></li>
                                <li><a href="#"><span className="fa fa-star gray-star" aria-hidden="true" /></a></li>
                            </ul>
                            <div className="clearfix"> </div>
                            </div>
                            <form action="#" method="post">
                            <input type="hidden" name="cmd" defaultValue="_cart" />
                            <input type="hidden" name="add" defaultValue={1} />
                            <input type="hidden" name="edu_item" defaultValue="Book12" />
                            <input type="hidden" name="amount" defaultValue={70.00} />
                            <button type="submit" className="edu-cart pedu-cart"><i className="fa fa-cart-plus" aria-hidden="true" /> Add to cart</button>
                            <a href="#" data-toggle="modal" data-target="#myModal1" />
                            </form>
                        </div>
                        </div>
                    </li>
                    </ul>
                </div>
                {/* /Slide3 */}
                </div>
                {/* //control-box */}
                <nav>
                <ul className="control-box pager">
                    <li><a data-slide="prev" href="#myCarousel1" className><i className="glyphicon glyphicon-chevron-left" /></a></li>
                    <li><a data-slide="next" href="#myCarousel1" className><i className="glyphicon glyphicon-chevron-right" /></a></li>
                </ul>
                </nav>
                {/* //control-box */}
                <div className="clearfix"> </div>
            </div>
            {/* /#myCarousel */}
            </div>
        </div>

        <div className="loadf-section">
        <div className="posf-grids">
          <div className="container">
            <h3 className="tittlef-agileits-w3layouts">Achieve more with grounding coaching sessions.</h3>
            <div className="col-md-4 posf-left">
              <div className="pos1">
                <a href="courses.html">Courses</a>
                <p className="paragraphf white-clrf">Pellentesque convallis diam consequat</p>
              </div>
              <div className="pos2">
                <a href="marketing.html">Marketing</a>
                <p className="paragraphf white-clrf">Pellentesque convallis diam consequat</p>
              </div>
            </div>
            <div id="loader">
              <div className="dot" />
              <div className="dot" />
              <div className="dot" />
              <div className="dot" />
              <div className="dot" />
              <div className="dot" />
              <div className="dot" />
              <div className="dot" />
              <div className="lading" />
            </div>
            <div className="col-md-4 posf-right">
              <div className="pos3">
                <a href="development.html">Development</a>
                <p className="paragraphf white-clrf">Pellentesque convallis diam consequat</p>
              </div>
              <div className="pos4">
                <a href="business.html">Business</a>
                <p className="paragraphf white-clrf">Pellentesque convallis diam consequat</p>
              </div>
            </div>
            <div className="clearfix"> </div>
            <div className="posf-btm">
              <div className="pos5">
                <a href="maths.html">Maths</a>
                <p className="paragraphf white-clrf">Pellentesque convallis diam consequat</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="reviewf-main">
        <div className="container">
          <h3 className="tittlef-agileits-w3layouts">Amazing Client Stories</h3>
          {/* reviewsf-left */}
          <div className="col-md-6 reviewsf-left">
            <div className="reviewsf-left">
              <div className="news-grids-bottom">
                {/* cycler */}
                <div id="design" className="date">
                  <div id="cycler">
                    <div className="date-text">
                      <img src="images/tf1.jpg" alt=" " className="img-responsive" />
                      <div className="clientf-info">
                        <span className="fa fa-quote-left" aria-hidden="true" />
                        <p>Pellentesque convallis diam consequat magna vulputate malesuada. Cras a ornare elit.</p>
                        <h6>Elizabeth Harper</h6>
                      </div>
                      <div className="clearfix"> </div>
                    </div>
                    <div className="date-text">
                      <img src="images/tf2.jpg" alt=" " className="img-responsive" />
                      <div className="clientf-info">
                        <span className="fa fa-quote-left" aria-hidden="true" />
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet lectus turpis. </p>
                        <h6>Anthony</h6>
                      </div>
                      <div className="clearfix"> </div>
                    </div>
                    <div className="date-text">
                      <img src="images/tf3.jpg" alt=" " className="img-responsive" />
                      <div className="clientf-info">
                        <span className="fa fa-quote-left" aria-hidden="true" />
                        <p>Pellentesque convallis diam consequat magna vulputate malesuada. Cras a ornare elit.</p>
                        <h6>Karen smith</h6>
                      </div>
                      <div className="clearfix"> </div>
                    </div>
                  </div>
                </div>
                {/* //cycler */}
              </div>
            </div>
          </div>
          {/* //reviewsf-left */}
          <div className="col-md-6 reviewsf-right">
            <h3 className="sub-w3ls-headf">Pellentesque convallis diam <span>consequat magna</span> vulputate malesuada</h3>
            <p className="paragraphf"><span className="fa fa-repeat" aria-hidden="true" /> Pellentesque convallis diam consequat magna vulputate malesuada.
              Cras a ornare elit. Nulla viverra pharetra sem, eget pulvinar neque pharetra ac.</p>
            <p className="paragraphf"><span className="fa fa-repeat" aria-hidden="true" /> Lorem Ipsum convallis diam consequat magna vulputate malesuada.
              Cras a ornare elit. Nulla viverra pharetra sem, eget pulvinar neque pharetra ac.</p>
            <div className="buttonf-styl">
              <a href="contact.html">Contact Us</a>
            </div>
          </div>
          <div className="clearfix"> </div>
        </div>
      </div>

      <div className="mobile-app">
        <div className="container">
          <div className="col-md-6 app-info">
            <h3 className="tittlef-agileits-w3layouts">Mobile App</h3>
            <p className="paragraphf">Nam arcu mauris, tincidunt sed convallis non, egestas ut lacus. Cras sapien urna, malesuada ut varius consequat, hendrerit
              nisl. Aliquam vestibulum, odio non ullamcorper malesuada.</p>
            <div className="app-devices">
              <a href="#"><img src="images/app.png" alt="" /></a>
              <a href="#"><img src="images/app1.png" alt="" /></a>
              <div className="clearfix"> </div>
            </div>
            <p className="paragraphf"><a href="#">Click here </a>to know more about apps.</p>
          </div>
          <div className="col-md-6 app-img">
            <img src="images/screens.png" alt=" " className="img-responsive" />
          </div>
          <div className="clearfix" />
        </div>
      </div>
        
        </div>

    
        
        );
}

export default Banner;