import { Paper, Typography } from "@mui/material";

import AppInput from "../Common/Input";
import AppButton from "../Common/Button";

const AIInputPanel = ({
    query,
    setQuery,
    onClick,
    loading
})=>{

    return(

        <Paper sx={{p:3}}>

            <Typography
                variant="h6"
                mb={2}
            >
                Ask AI
            </Typography>

            <AppInput
                label="Ask anything..."
                multiline
                rows={6}
                value={query}
                onChange={(e)=>setQuery(e.target.value)}
            />

            <AppButton
                fullWidth
                sx={{mt:3}}
                onClick={onClick}
                disabled={loading}
            >
                {
                    loading
                    ?
                    "Thinking..."
                    :
                    "Ask AI"
                }

            </AppButton>

        </Paper>

    );

}

export default AIInputPanel;