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
      for (const row of $rows) {
        console.log(row.innerText.replace(/ /g,''))
        console.log(row.innerText.replace(/ /g,'').split("\n\n"))
        // Do 20. Juni 2024\n\nBlaue Papiertonne\n\nalle 4 Wochen
      }
    })
  })
})