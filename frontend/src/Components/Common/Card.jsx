import { Card, CardContent } from "@mui/material";

const AppCard = ({ children, sx = {} }) => {

    return (

        <Card
            elevation={2}
            sx={{
                borderRadius: 3,
                ...sx
            }}
        >
            <CardContent>

                {children}

            </CardContent>
        </Card>

    );

};

export default AppCard;