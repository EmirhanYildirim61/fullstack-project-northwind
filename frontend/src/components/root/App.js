import React from "react";
import {Container} from "reactstrap";
import Navi from "../navi/Navi";
import Dashboard from "./Dashboard";
import {Route, Routes, useParams} from "react-router-dom"
import CartDetail from "../cart/CartDetail";
import AddOrUpdateProduct from "../products/AddOrUpdateProduct";
import NotFound from "../common/NotFound";

function AddOrUpdateProductRoute() {
    const {productId} = useParams()
    return <AddOrUpdateProduct productId={productId} />
}

function App() {
    return (
        <Container>
            <Navi />
            <Routes>
                <Route path="/" element={<Dashboard />} />
                <Route path="/product" element={<Dashboard />} />
                <Route path="/cart" element={<CartDetail />} />
                <Route path="/saveproduct/:productId" element={<AddOrUpdateProductRoute />} />
                <Route path="/saveproduct" element={<AddOrUpdateProductRoute />} />
                <Route path="*" element={<NotFound />} />
            </Routes>
        </Container>
    );
}

export default App;
