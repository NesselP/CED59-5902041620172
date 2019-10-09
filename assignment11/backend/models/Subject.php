<?php
namespace backend\models;

use yii\behaviors\TimestampBehavior;
use yii\behaviors\BlameableBehavior;

class Subject extends \common\models\Subject
{
    public function behaviors()
    {
        return [
            TimestampBehavior::class,
            BlameableBehavior::class
        ];
    }
    public function rules(){
        return [
            ['name', 'required','massage'=>'please fill data']
            ['name', 'email','massage'=>'fill type email ja']
        ];
    }
}
