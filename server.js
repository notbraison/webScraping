/* This is a webscraper whose main  aim is to collect data of all football players names and ages 
in all champions league matches across time
and get the average age
 */
import puppeteer from 'puppeteer'//import libraries and all its helper functions

//url of ucl finals on wikipidia
//url of football player ages/birth years 
const url = 'https://en.wikipedia.org/wiki/List_of_European_Cup_and_UEFA_Champions_League_finals';
const url1 = 'https://fbref.com/en/';

