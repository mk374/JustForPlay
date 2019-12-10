import React from 'react';
import PropTypes from 'prop-types'

import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Start from './Start/Start'
import HomePage from './Home/HomePage';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Grid from '@material-ui/core/Grid';

import {withStyles} from '@material-ui/styles';

const START_PAGE = 0;
const USER_HOME_PAGE = 1;

const styles = theme => ({
  card: {
    minWidth: 300,
    width: 500
  }
});

class App extends React.Component {

  constructor(props){
    super(props);
    this.state={
      page: START_PAGE,
      groups: [],
      user: {}
    }
  }

  changeScreenState = () => {
    // keep it between 1 and 0
    var currState = this.state.page;
    this.setState({
      page: currState === START_PAGE ? USER_HOME_PAGE : START_PAGE
    })
  }

  updateGroups = (groups) => {
    this.setState({
      groups : groups
    })
  }

  updateUser = (user) => {
    this.setState({
      user : user
    })
  }

  render() {

    var childpage;
    const { classes } = this.props;

    switch(this.state.page) {
          case START_PAGE:
            childpage = (
              <Grid
                  container
                  spacing={0}
                  direction="column"
                  alignItems="center"
                  justify="center"
                  style={{ minHeight: '100vh' }}
              >
                <Grid item>
                  <Card className={classes.card}>
                    <CardContent>
                      <Start onLogin={this.changeScreenState} updateGroups={this.updateGroups} updateUser={this.updateUser}></Start>
                    </CardContent>
                  </Card>
                </Grid>
              </Grid>
            )
            break;
          case USER_HOME_PAGE:
            childpage = (
              <HomePage user={this.state.user} onLogout={this.changeScreenState} groups={this.state.groups}></HomePage>
            )
            break;
          default:
            childpage = (
              null
            )
    }
    return (

        <div className="App">
          {childpage}
        </div>
      );
  }
}

HomePage.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(App);
