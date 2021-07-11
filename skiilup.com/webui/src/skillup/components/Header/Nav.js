import React from 'react';

import { Link } from 'react-router-dom';


function Nav(props) {
    return (
        <nav className="navbar navbar-inverse">
            <div className="navbar-header">
                <button className="navbar-toggle" type="button" data-toggle="collapse" data-target=".js-navbar-collapse">
                <span className="sr-only">Toggle navigation</span>
                <span className="icon-bar" />
                <span className="icon-bar" />
                <span className="icon-bar" />
                </button>
            </div>
            <div className="collapse navbar-collapse js-navbar-collapse">
                <ul className="nav navbar-nav">
                <li className="dropdown mega-dropdown">
                    <a href="#" className="dropdown-toggle" data-toggle="dropdown">Courses <span className="caret" /></a>
                    <ul className="dropdown-menu mega-dropdown-menu">
                    <li className="col-md-3 col-sm-4 col-xs-6">
                        <ul>
                        <li className="dropdown-header">Type 1</li>
                        <li><a href="courses.html">Core IT Skills</a></li>
                        <li><a href="courses.html">Data Science</a></li>
                        <li><a href="courses.html">Databases</a></li>
                        <li><a href="courses.html">Game Development</a></li>
                        </ul>
                    </li>
                    <li className="col-md-3 col-sm-4 col-xs-6">
                        <ul>
                        <li className="dropdown-header">Type 2</li>
                        <li><a href="courses.html">Hardware</a></li>
                        <li><a href="courses.html">IT Management</a></li>
                        <li><a href="courses.html">Mobile Apps</a></li>
                        <li><a href="courses.html">Network And Security</a></li>
                        </ul>
                    </li>
                    <li className="col-md-3 col-sm-4 col-xs-6">
                        <ul>
                        <li className="dropdown-header">Type 3</li>
                        <li><a href="courses.html">Core IT Skills</a></li>
                        <li><a href="courses.html">Data Science</a></li>
                        <li><a href="courses.html">Databases</a></li>
                        <li><a href="courses.html">Game Development</a></li>
                        </ul>
                    </li>
                    <li className="col-md-3 col-sm-4 col-xs-6">
                        <ul>
                        <li className="dropdown-header">Blog Styles</li>
                        <li><a href="blog_1.html">Simple</a></li>
                        <li><a href="blog_4.html">Creative</a></li>
                        <li><a href="blog_2.html">2-col Grids</a></li>
                        <li><a href="blog_3.html">3-col Grids</a></li>
                        </ul>
                    </li>
                    </ul>
                </li>
                <li className="dropdown mega-dropdown">
                    <a href="#" className="dropdown-toggle" data-toggle="dropdown">Marketing <span className="caret" /></a>
                    <ul className="dropdown-menu mega-dropdown-menu">
                    <li className="col-md-3 col-sm-4 col-xs-6">
                        <ul>
                        <li className="dropdown-header">Type 1</li>
                        <li><a href="marketing.html">Digital Marketing</a></li>
                        <li><a href="marketing.html">Marketing Management</a></li>
                        <li><a href="marketing.html">Public Relations</a></li>
                        <li><a href="marketing.html">Social Media Marketing</a></li>
                        </ul>
                    </li>
                    <li className="col-md-3 col-sm-4 col-xs-6">
                        <ul>
                        <li className="dropdown-header">Type 2</li>
                        <li><a href="marketing.html">Digital Marketing</a></li>
                        <li><a href="marketing.html">Marketing Management</a></li>
                        <li><a href="marketing.html">Public Relations</a></li>
                        <li><a href="marketing.html">Social Media Marketing</a></li>
                        </ul>
                    </li>
                    <li className="col-md-3 col-sm-4 col-xs-6">
                        <ul>
                        <li className="dropdown-header">Type 3</li>
                        <li><a href="marketing.html">Digital Marketing</a></li>
                        <li><a href="marketing.html">Marketing Management</a></li>
                        <li><a href="marketing.html">Public Relations</a></li>
                        <li><a href="marketing.html">Social Media Marketing</a></li>
                        </ul>
                    </li>
                    <li className="col-md-3 col-sm-4 col-xs-6">
                        <ul>
                        <li className="dropdown-header">Blog Styles</li>
                        <li><a href="blog_1.html">Simple</a></li>
                        <li><a href="blog_4.html">Creative</a></li>
                        <li><a href="blog_2.html">2-col Grids</a></li>
                        <li><a href="blog_3.html">3-col Grids</a></li>
                        </ul>
                    </li>
                    </ul>
                </li>
                <li className="dropdown mega-dropdown">
                    <a href="#" className="dropdown-toggle" data-toggle="dropdown">Development <span className="caret" /></a>
                    <ul className="dropdown-menu mega-dropdown-menu">
                    <li className="col-md-3 col-sm-4 col-xs-6">
                        <ul>
                        <li className="dropdown-header">Type 1</li>
                        <li><a href="development.html">Web Development</a></li>
                        <li><a href="development.html">Mobile Apps</a></li>
                        <li><a href="development.html">Programming Languages</a></li>
                        <li><a href="development.html">Game Development</a></li>
                        </ul>
                    </li>
                    <li className="col-md-3 col-sm-4 col-xs-6">
                        <ul>
                        <li className="dropdown-header">Type 2</li>
                        <li><a href="development.html">Databases</a></li>
                        <li><a href="development.html">Software Testing</a></li>
                        <li><a href="development.html">Software Engineering</a></li>
                        <li><a href="development.html">Development Tools</a></li>
                        </ul>
                    </li>
                    <li className="col-md-3 col-sm-4 col-xs-6">
                        <ul>
                        <li className="dropdown-header">Type 3</li>
                        <li><a href="development.html">Web Development</a></li>
                        <li><a href="development.html">Mobile Apps</a></li>
                        <li><a href="development.html">Programming Languages</a></li>
                        <li><a href="development.html">Game Development</a></li>
                        </ul>
                    </li>
                    <li className="col-md-3 col-sm-4 col-xs-6">
                        <ul>
                        <li className="dropdown-header">Blog Styles</li>
                        <li><a href="blog_1.html">Simple</a></li>
                        <li><a href="blog_4.html">Creative</a></li>
                        <li><a href="blog_2.html">2-col Grids</a></li>
                        <li><a href="blog_3.html">3-col Grids</a></li>
                        </ul>
                    </li>
                    </ul>
                </li>
                <li className="dropdown mega-dropdown">
                    <a href="#" className="dropdown-toggle" data-toggle="dropdown">Business <span className="caret" /></a>
                    <ul className="dropdown-menu mega-dropdown-menu">
                    <li className="col-md-3 col-sm-4 col-xs-6">
                        <ul>
                        <li className="dropdown-header">Type 1</li>
                        <li><a href="business.html">Communications</a></li>
                        <li><a href="business.html">E-Commerce</a></li>
                        <li><a href="business.html">Entrepreneurship</a></li>
                        <li><a href="business.html">Finance</a></li>
                        </ul>
                    </li>
                    <li className="col-md-3 col-sm-4 col-xs-6">
                        <ul>
                        <li className="dropdown-header">Type 2</li>
                        <li><a href="business.html">Human Resources</a></li>
                        <li><a href="business.html">Leadership &amp; Management</a></li>
                        <li><a href="business.html">Operations</a></li>
                        <li><a href="business.html">Project Management</a></li>
                        </ul>
                    </li>
                    <li className="col-md-3 col-sm-4 col-xs-6">
                        <ul>
                        <li className="dropdown-header">Type 3</li>
                        <li><a href="business.html">Sales</a></li>
                        <li><a href="business.html">Tourism &amp; Hospitality</a></li>
                        <li><a href="business.html">Strategy</a></li>
                        <li><a href="business.html">Business Law</a></li>
                        </ul>
                    </li>
                    <li className="col-md-3 col-sm-4 col-xs-6">
                        <ul>
                        <li className="dropdown-header">Blog Styles</li>
                        <li><a href="blog_1.html">Simple</a></li>
                        <li><a href="blog_4.html">Creative</a></li>
                        <li><a href="blog_2.html">2-col Grids</a></li>
                        <li><a href="blog_3.html">3-col Grids</a></li>
                        </ul>
                    </li>
                    </ul>
                </li>
                <li className="dropdown mega-dropdown">
                    <a href="#" className="dropdown-toggle" data-toggle="dropdown">Maths <span className="caret" /></a>
                    <ul className="dropdown-menu mega-dropdown-menu">
                    <li className="col-md-3 col-sm-4 col-xs-6">
                        <ul>
                        <li className="dropdown-header">Type 1</li>
                        <li><a href="maths.html">Algebra</a></li>
                        <li><a href="maths.html">Calculus</a></li>
                        <li><a href="maths.html">Core Maths Skills</a></li>
                        <li><a href="maths.html">Geometry</a></li>
                        </ul>
                    </li>
                    <li className="col-md-3 col-sm-4 col-xs-6">
                        <ul>
                        <li className="dropdown-header">Type 2</li>
                        <li><a href="maths.html">Probability &amp; Statistics</a></li>
                        <li><a href="maths.html">Series and Sequences</a></li>
                        <li><a href="maths.html">Calculus</a></li>
                        <li><a href="maths.html">Core Maths Skills</a></li>
                        </ul>
                    </li>
                    <li className="col-md-3 col-sm-4 col-xs-6">
                        <ul>
                        <li className="dropdown-header">Type 3</li>
                        <li><a href="maths.html">All Test Prep</a></li>
                        <li><a href="maths.html">Test Taking Skills</a></li>
                        <li><a href="maths.html">Educational Development</a></li>
                        <li><a href="maths.html">Core Maths Skills</a></li>
                        </ul>
                    </li>
                    <li className="col-md-3 col-sm-4 col-xs-6">
                        <ul>
                        <li className="dropdown-header">Blog Styles</li>
                        <li><a href="blog_1.html">Simple</a></li>
                        <li><a href="blog_4.html">Creative</a></li>
                        <li><a href="blog_2.html">2-col Grids</a></li>
                        <li><a href="blog_3.html">3-col Grids</a></li>
                        </ul>
                    </li>
                    </ul>
                </li>
                <li><Link to="/about">About</Link>, {' '}</li>
                <li><a href="contact.html">Contact</a></li>
                </ul>
            </div>
            
            </nav>
    );
}

export default Nav;