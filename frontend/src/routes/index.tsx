import React from 'react';
import {Route, Switch} from 'react-router-dom';
import AirAstana from '../pages/AirAstana';
import Start from '../pages/Start';

const Routes: React.FC = () => (
    <Switch>
        <Route exact path="/" component={Start}/>
        <Route exact path="/airastana" component={AirAstana}/>
    </Switch>
);

export default Routes;