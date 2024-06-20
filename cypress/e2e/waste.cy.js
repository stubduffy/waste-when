function callGithub(text) {
  cy.request({
    method: 'POST',
    url: '/login_with_form',
    body: {
      username: 'jane.lane',
      password: 'password123',
    },
  })
}

describe('template spec', () => {
  it('passes', () => {
    cy.visit('https://www.stadtreinigung.hamburg/abfuhrkalender/')
    cy.findByPlaceholderText('Straße').type('Fünfhausener Straße')
    cy.contains('Fünfhausener Straße').click()
    cy.get('[data-options-name=housenumbers]').select('68')
    cy.get('input[name="tx_srh_pickups[isAllowedOwner]"]').check()
    cy.contains('Termine suchen').click()
    cy.get('tr').then(($rows) => {
      let data = {
        "paper": "",
        "rest": "",
        "yellow": "",
        "bio": ""
      }
      for (const row of $rows) {
        // example: Do 20. Juni 2024\n\nBlaue Papiertonne\n\nalle 4 Wochen
        const items = row.innerText.replace(/ /g,'').split("\n\n")
        console.log(items)
        if (data.paper == "" && items[1] != undefined && items[1].includes("Blaue")) {
          data.paper = items[0]
        }
        if (data.rest == "" && items[1] != undefined && items[1].includes("Schwarze")) {
          data.rest = items[0]
        }
        if (data.bio == "" && items[1] != undefined && items[1].includes("Grüne")) {
          data.bio = items[0]
        }
        if (data.yellow == "" && items[1] != undefined && items[1].includes("Gelbe")) {
          data.yellow = items[0]
        }
      }

      cy.writeFile('cal.json', data)
    })
  })
})