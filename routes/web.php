<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

	

Route::POST('/tes', 'BCAController@cek');
// Route::group( ['middleware' => 'auth' ], function()
// {

Route::get('/dashboard', 'IndexController@index');
Route::get('/loginbri', 'BRIController@index');
Route::get('/loginbca', 'BCAController@index');
Route::get('/loginbtn', 'BTNController@index');
Route::get('/cekmutasiku', 'CekMutasiController@index');
Route::get('/pengguna', 'PenggunaController@index');
Route::get('/riwayat', 'RiwayatController@index');
Auth::routes();
Route::get('/logout', '\App\Http\Controllers\Auth\LoginController@logout');

// 
// });

Route::get('/home', 'HomeController@index')->name('home');
