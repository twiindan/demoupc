Feature: Geoencoding
    As a user
    I want to know the country code of localtion
    in order to improve my geography knowledge

    Scenario Outline: Retrieve the geolocation with city name given and without sensor
        Given a <city> name
        When I request the geoencoding of the city
        Then I obtain the <city> name with the <country_code>

        Examples:
            |   city            |   country_code    |
            |   Barcelona       |   ES              |
            |   Paris           |   FR              |
            |   San+Francisco   |   US              |



    Scenario Outline: Retrieve zero results if city not exist
        Given a <city> name
        When I request the geoencoding of the city
        Then I obtain a response with status "ZERO_RESULTS"

        Examples:
            |   city            |
            |   sdfjksd         |
            |   me llamo pepito |
            |   FIB   FOREVER   |


    Scenario Outline: Incorrect requests
        Given a <city> name
        When I request the geoencoding without <sensor_parameter> or <city>
        Then I obtain an <Error_Code>

        Examples:
            |   city            |   sensor_parameter    |   Error_Code  |
            |   Barcelona       |   null                |   404         |
            |   null            |   False               |   404         |
            |   Barcelona       |   testing             |   404         |


    Scenario Outline: Retrieve the geolocation with city name misspelling
        Given a <city> name
        When I request the geoencoding of the city
        Then I obtain the <city> name with the <country_code>

        Examples:
            |   city            |   country_code    |
            |   Madrit          |   ES              |
            |   Madril          |   ES              |
            |   Barcelon        |   ES              |


