import React from 'react';

import { Link } from 'react-router-dom';
function MiddleHeader(props) {
    return (
        <div className="header-middle">
            <div className="container">
                <div className="logof-w3-agile">
                <h1><Link to="/">Grounding</Link>, {' '}</h1>
                </div>
                <div className="searchf-w3-agileits-headr">
                <form action="#" method="post">
                    <input type="search" name="Search" placeholder="Search for a Product..." required />
                    <button type="submit" className="btn btn-default search" aria-label="Left Align">
                    <i className="fa fa-search" aria-hidden="true"> </i>
                    </button>
                </form>
                </div>
                <div className="cart-mainf">
                <a className="shop" href="shop.html">Shop Now</a>
                </div>
                <div className="clearfix" />
            </div>
            </div>
    );
}

export default MiddleHeader;