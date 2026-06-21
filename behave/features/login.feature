Feature: Login en SauceDemo

  Scenario: Login exitoso con usuario válido
    Given que estoy en la página de login
    When inicio sesión con usuario "standard_user" y password "secret_sauce"
    Then debo ver la lista de productos

  Scenario: Login fallido con usuario inválido
    Given que estoy en la página de login
    When inicio sesión con usuario "locked_out_user" y password "secret_sauce"
    Then debo ver un mensaje de error de login