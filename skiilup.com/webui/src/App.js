import React, { Suspense, lazy } from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Main from './layouts/Main'; // fallback for lazy pages
const { PUBLIC_URL } = process.env;
const Index = lazy(() => import('./pages/Index'));
const About = lazy(() => import('./pages/About'));


const App = () => (
  <BrowserRouter basename={PUBLIC_URL}>
    <Suspense fallback={<Main />}>
      <Switch>
        <Route exact path="/" component={Index} />
        <Route path="/About" component={About} />
        
      </Switch>
    </Suspense>
  </BrowserRouter>
);

export default App;


