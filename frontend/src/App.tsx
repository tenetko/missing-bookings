import React from 'react';
import {Layout} from 'antd';
import LeftMenu from "./components/LeftMenu";
import Routes from "./routes";
const {Content, Footer} = Layout;

const App: React.FC = () => {
    return(
        <Layout style={{minHeight: '100vh'}}>
            <LeftMenu/>
            <Layout>
                <Content style={{margin: '0 16px'}}>
                    <div style={{padding:24, background: '#fff', minHeight: 360}}>
                        <Routes/>
                    </div>
                </Content>
                <Footer style={{textAlign: 'center'}}>
                </Footer>
            </Layout>
        </Layout>
    )
};

export default App;
