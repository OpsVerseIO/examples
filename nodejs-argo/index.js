const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello OpsVerse User! This is a Sample NodeJS App')
})

app.listen(port, () => {
  console.log(`OpsVerse sample nodejs app listening on port ${port}`)
})

