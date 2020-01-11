<template>
  <div>
    <!------------------------------------------------新增查询div开始-------------------------------------------------->
    <div class="addAndSearch">
      <el-row :gutter="0">
        <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" class="addBox">
          <el-button icon="el-icon-plus" type="primary" @click="showAdd()" :loading="isLoading">新增</el-button>
        </el-col>
        <el-col :xs="18" :sm="18" :md="18" :lg="18" :xl="18" class="searchBox">
          <el-form :model="searchForm" class="searchForm" :rules="searchRules" ref="searchForm">
            <el-form-item label="" prop="name">
              <el-input v-model="searchForm.name" placeholder="请输入材料名称" clearable></el-input>
            </el-form-item>
            <el-form-item label="" class="lineTwoBtn lineTwoBtnBtn">
              <el-button icon="el-icon-search" type="primary" @click="search(searchForm.name)" :loading="isLoading">查询</el-button>
            </el-form-item>
          </el-form>
        </el-col>
      </el-row>
    </div>
    <!------------------------------------------------新增查询div结束-------------------------------------------------->
    <!------------------------------------------------列表开始--------------------------------------------------------->
    <el-table :data="materialList" class="materialTable" border>
      <el-table-column prop="name" label="材料名称" width="200" fixed="left">
      </el-table-column>
      <el-table-column prop="endDate" label="结束日期" width="120" fixed="left">
      </el-table-column>
      <el-table-column v-for="item in userList" :label="item.name" :key="item.id" min-width="460">
        <template slot-scope="scope">
          <div v-if="scope.row.requirementList.find(it => it.userId === item.id) !== undefined">
            <el-row :gutter="20">
              <el-col :span="16">
                <el-tag effect="dark" type="info" size="medium">需要：{{scope.row.requirementList.find(it => it.userId === item.id).requiredNumber}}个</el-tag>
                <el-tag effect="dark" type="success" size="medium">已有：{{scope.row.requirementList.find(it => it.userId === item.id).ownedNumber}}个</el-tag>
                <el-tag effect="dark" type="warning" size="medium" v-if="getDate(scope.row.endDate) > 0">每日：{{Math.ceil((scope.row.requirementList.find(it => it.userId === item.id).requiredNumber - scope.row.requirementList.find(it => it.userId === item.id).ownedNumber) / getDate(scope.row.endDate))}}个</el-tag>
                <el-tag effect="dark" type="danger" size="medium" v-else>活动已结束</el-tag>
              </el-col>
              <el-col :span="8" align="right">
                <el-button icon="el-icon-edit" type="primary" plain @click="showEditMaterial(item.id, scope.row.id, item.name, scope.row.name, scope.row.requirementList.find(it => it.userId === item.id).requiredNumber, scope.row.requirementList.find(it => it.userId === item.id).ownedNumber)" :loading="isLoading" size="mini"></el-button>
                <el-button icon="el-icon-delete" type="danger" plain @click="delMaterial(item.id, scope.row.id)" :loading="isLoading" size="mini"></el-button>
              </el-col>
            </el-row>
          </div>
          <div v-else>
            <el-row :gutter="20">
              <el-col :span="24" align="right">
                <el-button icon="el-icon-plus" type="primary" plain @click="showAddMaterial(item.id, scope.row.id, item.name, scope.row.name)" :loading="isLoading" size="mini"></el-button>
              </el-col>
            </el-row>
          </div>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="200" fixed="right">
        <template slot-scope="scope">
          <el-button icon="el-icon-edit" type="primary" @click="showEdit(scope.row.id)" :loading="isLoading" size="mini"></el-button>
          <el-button icon="el-icon-delete" type="danger" @click="del(scope.row.id)" :loading="isLoading" size="mini"></el-button>
        </template>
      </el-table-column>
    </el-table>
    <!------------------------------------------------列表结束--------------------------------------------------------->
    <!------------------------------------------------新增弹窗开始----------------------------------------------------->
    <el-dialog title="新增材料" :visible.sync="addFormVisible" width="400px" center :before-close="closeAdd">
      <el-form :model="addForm" ref="addForm" :rules="addFormRules" class="dialogForm">
        <el-form-item label="材料名称" prop="name">
          <el-input v-model="addForm.name" clearable></el-input>
        </el-form-item>
        <el-form-item label="结束日期" prop="endDate">
          <el-date-picker v-model="addForm.endDate" type="date" placeholder="选择日期"></el-date-picker>
        </el-form-item>
        <el-form-item class="btnBox">
          <el-button icon="el-icon-check" type="primary" @click="add()" :loading="isLoading">提交</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
    <!------------------------------------------------新增弹窗结束----------------------------------------------------->
    <!------------------------------------------------修改弹窗开始----------------------------------------------------->
    <el-dialog title="修改材料" :visible.sync="editFormVisible" width="400px" center :before-close="closeEdit">
      <el-form :model="editForm" ref="editForm" :rules="editFormRules" class="dialogForm">
        <el-form-item label="id" prop="id" v-show="false">
          <el-input v-model="editForm.id" disabled="disabled"></el-input>
        </el-form-item>
        <el-form-item label="材料名称" prop="name">
          <el-input v-model="editForm.name" clearable></el-input>
        </el-form-item>
        <el-form-item label="结束日期" prop="endDate">
          <el-date-picker v-model="editForm.endDate" type="date" placeholder="选择日期"></el-date-picker>
        </el-form-item>
        <el-form-item class="btnBox">
          <el-button icon="el-icon-check" type="primary" @click="edit()" :loading="isLoading">提交</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
    <!------------------------------------------------修改弹窗结束----------------------------------------------------->
    <!------------------------------------------------新增用户材料需求弹窗开始----------------------------------------->
    <el-dialog title="新增用户材料需求" :visible.sync="addMaterialFormVisible" width="400px" center :before-close="closeAddMaterial">
      <el-form :model="addMaterialForm" ref="addMaterialForm" class="dialogForm">
        <el-form-item label="userId" prop="userId" v-show="false">
          <el-input v-model="addMaterialForm.userId" disabled="disabled"></el-input>
        </el-form-item>
        <el-form-item label="materialId" prop="materialId" v-show="false">
          <el-input v-model="addMaterialForm.materialId" disabled="disabled"></el-input>
        </el-form-item>
        <el-form-item label="用户姓名" prop="userName">
          <el-input v-model="addMaterialForm.userName" disabled="disabled"></el-input>
        </el-form-item>
        <el-form-item label="材料名称" prop="materialName">
          <el-input v-model="addMaterialForm.materialName" disabled="disabled"></el-input>
        </el-form-item>
        <el-form-item label="需要" prop="requiredNumber">
          <el-input-number class="value" v-model="addMaterialForm.requiredNumber" :precision="0" :step="1" :min="0" :max="99999" controls-position="right"></el-input-number>
        </el-form-item>
        <el-form-item label="已有" prop="ownedNumber">
          <el-input-number class="value" v-model="addMaterialForm.ownedNumber" :precision="0" :step="1" :min="0" :max="99999" controls-position="right"></el-input-number>
        </el-form-item>
        <el-form-item class="btnBox">
          <el-button icon="el-icon-check" type="primary" @click="addMaterial()" :loading="isLoading">提交</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
    <!------------------------------------------------新增用户材料需求弹窗结束----------------------------------------->
    <!------------------------------------------------修改用户材料需求弹窗开始----------------------------------------->
    <el-dialog title="修改用户材料需求" :visible.sync="editMaterialFormVisible" width="400px" center :before-close="closeEditMaterial">
      <el-form :model="editMaterialForm" ref="editMaterialForm" class="dialogForm">
        <el-form-item label="userId" prop="userId" v-show="false">
          <el-input v-model="editMaterialForm.userId" disabled="disabled"></el-input>
        </el-form-item>
        <el-form-item label="materialId" prop="materialId" v-show="false">
          <el-input v-model="editMaterialForm.materialId" disabled="disabled"></el-input>
        </el-form-item>
        <el-form-item label="用户姓名" prop="userName">
          <el-input v-model="editMaterialForm.userName" disabled="disabled"></el-input>
        </el-form-item>
        <el-form-item label="材料名称" prop="materialName">
          <el-input v-model="editMaterialForm.materialName" disabled="disabled"></el-input>
        </el-form-item>
        <el-form-item label="需要" prop="requiredNumber">
          <el-input-number class="value" v-model="editMaterialForm.requiredNumber" :precision="0" :step="1" :min="0" :max="99999" controls-position="right"></el-input-number>
        </el-form-item>
        <el-form-item label="已有" prop="ownedNumber">
          <el-input-number class="value" v-model="editMaterialForm.ownedNumber" :precision="0" :step="1" :min="0" :max="99999" controls-position="right"></el-input-number>
        </el-form-item>
        <el-form-item class="btnBox">
          <el-button icon="el-icon-check" type="primary" @click="editMaterial()" :loading="isLoading">提交</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
    <!------------------------------------------------修改用户材料需求弹窗结束----------------------------------------->
  </div>
</template>

<script>
import moment from 'moment'

export default {
  data: function () {
    return {
      isLoading: false,
      // 搜索
      searchForm: {
        name: null
      },
      searchName: null,
      searchRules: {
        name: [
          { max: 20, message: '材料名称在20个字符以内', trigger: 'blur' }
        ]
      },
      // 列表
      materialList: [],
      userList: [],
      // 新增材料
      addFormVisible: false,
      addForm: {
        name: null,
        endDate: null
      },
      addFormRules: {
        name: [
          { required: true, message: '请输入材料名称', trigger: 'blur' },
          { max: 20, message: '材料名称在20个字符以内', trigger: 'blur' }
        ],
        endDate: [
          { required: true, message: '请选择结束日期', trigger: 'blur' }
        ]
      },
      // 修改材料
      editFormVisible: false,
      editForm: {
        id: 0,
        name: null,
        endDate: null
      },
      editFormRules: {
        name: [
          { required: true, message: '请输入材料名称', trigger: 'blur' },
          { max: 20, message: '材料名称在20个字符以内', trigger: 'blur' }
        ],
        endDate: [
          { required: true, message: '请选择结束日期', trigger: 'blur' }
        ]
      },
      // 新增用户材料需求
      addMaterialFormVisible: false,
      addMaterialForm: {
        userId: null,
        materialId: null,
        userName: null,
        materialName: null,
        requiredNumber: 0,
        ownedNumber: 0
      },
      // 新增用户材料需求
      editMaterialFormVisible: false,
      editMaterialForm: {
        userId: null,
        materialId: null,
        userName: null,
        materialName: null,
        requiredNumber: 0,
        ownedNumber: 0
      }
    }
  },
  mounted: function () {
    this.materialList = [
      {id: 1, name: '龙之硬币', endDate: '2020-01-14', requirementList: [{userId: 1, requiredNumber: 50, ownedNumber: 10}, {userId: 2, requiredNumber: 40, ownedNumber: 20}]},
      {id: 2, name: '苍穹碎片', endDate: '2020-01-10', requirementList: [{userId: 2, requiredNumber: 7, ownedNumber: 0}]},
      {id: 3, name: '辉煌的金色气息', endDate: '2020-01-14', requirementList: []}
    ]
    this.userList = [
      {id: 1, name: '华晓澄'},
      {id: 2, name: '李征'}
    ]
    // this.search(null)
  },
  methods: {
    // 计算结束日期与今天的差值
    getDate: function (endDate) {
      return moment(endDate).diff(moment(new Date()), 'days') + 1
    },
    // 查询材料列表
    search: function (name) {
      this.$refs['searchForm'].validate((valid) => {
        if (valid) {
          this.searchName = name
          this.isLoading = true
          this.axios.get('/api/material/list?name=' + this.searchName).then(res => {
            console.log('材料列表', res)
            this.materialList = res.data.data.materialList
            this.userList = res.data.data.userList
            this.isLoading = false
          }).catch(err => {
            console.log('材料列表出错', err)
            this.isLoading = false
          })
          // this.materialList = [
          //   {id: 1, name: '反物质粒子', requirementList: [{userId: 1, requiredNumber: 100, ownedNumber: 50}, {userId: 2, requiredNumber: 120, ownedNumber: 70}]},
          //   {id: 2, name: '苍穹碎片', requirementList: [{userId: 1, requiredNumber: 300, ownedNumber: 200}]},
          //   {id: 3, name: '精炼的时空石', requirementList: [{userId: 1, requiredNumber: 10, ownedNumber: 6}, {userId: 2, requiredNumber: 8, ownedNumber: 4}]}
          // ]
          // this.userList = [{id: 1, name: 'lz'}, {id: 2, name: 'hxc'}]
        } else {
          this.$message({
            type: 'error',
            message: '查询格式错误'
          })
          return false
        }
      })
    },
    // 显示新增材料弹窗
    showAdd: function () {
      this.addFormVisible = true
    },
    // 关闭新增材料弹窗
    closeAdd: function (done) {
      this.$confirm('确认关闭吗？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$refs['addForm'].resetFields()
        done()
      }).catch(() => {})
    },
    // 新增材料
    add: function () {
      this.$refs['addForm'].validate((valid) => {
        if (valid) {
          this.isLoading = true
          this.axios.post('/api/material/save', this.addForm).then(res => {
            console.log('新增', res)
            this.$message({
              type: 'success',
              message: '新增成功'
            })
            this.$refs['addForm'].resetFields()
            this.addFormVisible = false
            this.search(this.searchName)
            this.isLoading = false
          }).catch(err => {
            console.log('新增出错', err)
            this.isLoading = false
          })
        } else {
          this.$message({
            type: 'error',
            message: '提交格式错误'
          })
        }
      })
    },
    // 显示修改材料弹窗
    showEdit: function (id) {
      this.isLoading = true
      this.axios.get('/api/material/get?id=' + id).then(res => {
        console.log('查询单个材料', res)
        this.editFormVisible = true
        this.$nextTick(() => { // resetFields初始化到第一次打开dialog时里面的form表单里的值，所以先渲染form表单，后改变值，这样resetFields后未空表单
          this.editForm.id = res.data.data.id
          this.editForm.name = res.data.data.name
        })
        this.isLoading = false
      }).catch(err => {
        console.log('查询单个材料出错', err)
        this.isLoading = false
      })
    },
    // 关闭修改材料弹窗
    closeEdit: function (done) {
      this.$confirm('确认关闭吗？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$refs['editForm'].resetFields()
        done()
      }).catch(() => {})
    },
    // 修改材料
    edit: function () {
      this.$refs['editForm'].validate((valid) => {
        if (valid) {
          this.isLoading = true
          this.axios.post('/api/material/update', this.editForm).then(res => {
            console.log('修改材料', res)
            this.$message({
              type: 'success',
              message: '修改成功'
            })
            this.$refs['editForm'].resetFields()
            this.editFormVisible = false
            this.search(this.searchName)
            this.isLoading = false
          }).catch(err => {
            console.log('修改材料出错', err)
            this.isLoading = false
          })
        } else {
          this.$message({
            type: 'error',
            message: '提交格式错误'
          })
        }
      })
    },
    // 删除材料
    del: function (id) {
      this.$confirm('确认删除这条记录吗？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.isLoading = true
        this.axios.post('/api/material/remove', {id: id}).then(res => {
          console.log('删除材料', res)
          this.$message({
            type: 'success',
            message: '删除成功 '
          })
          this.search(this.searchName)
          this.isLoading = false
        }).catch(err => {
          console.log('删除材料出错', err)
          this.isLoading = false
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '删除已取消'
        })
      })
    },
    // 显示新增用户材料需求弹窗
    showAddMaterial: function (userId, materialId, userName, materialName) {
      this.addMaterialFormVisible = true
      this.$nextTick(() => { // resetFields初始化到第一次打开dialog时里面的form表单里的值，所以先渲染form表单，后改变值，这样resetFields后未空表单
        this.addMaterialForm.userId = userId
        this.addMaterialForm.materialId = materialId
        this.addMaterialForm.userName = userName
        this.addMaterialForm.materialName = materialName
      })
    },
    // 关闭新增用户材料需求弹窗
    closeAddMaterial: function (done) {
      this.$confirm('确认关闭吗？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$refs['addMaterialForm'].resetFields()
        done()
      }).catch(() => {})
    },
    // 新增用户材料需求
    addMaterial: function () {
      this.$refs['addMaterialForm'].validate((valid) => {
        if (valid) {
          this.isLoading = true
          this.axios.post('/api/material/saveRequirement', this.addMaterialForm).then(res => {
            console.log('新增用户材料需求', res)
            this.$message({
              type: 'success',
              message: '新增成功'
            })
            this.$refs['addMaterialForm'].resetFields()
            this.addMaterialFormVisible = false
            this.search(this.searchName)
            this.isLoading = false
          }).catch(err => {
            console.log('新增用户材料需求出错', err)
            this.isLoading = false
          })
        } else {
          this.$message({
            type: 'error',
            message: '提交格式错误'
          })
        }
      })
    },
    // 删除用户材料需求
    delMaterial: function (userId, materialId) {
      this.$confirm('确认删除这条记录吗？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.isLoading = true
        this.axios.post('/api/material/removeRequirement', {userId: userId, materialId: materialId}).then(res => {
          console.log('删除用户材料需求', res)
          this.$message({
            type: 'success',
            message: '删除成功 '
          })
          this.search(this.searchName)
          this.isLoading = false
        }).catch(err => {
          console.log('删除用户材料需求出错', err)
          this.isLoading = false
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '删除已取消'
        })
      })
    },
    // 显示修改用户材料需求弹窗
    showEditMaterial: function (userId, materialId, userName, materialName, requiredNumber, ownedNumber) {
      this.editMaterialFormVisible = true
      this.$nextTick(() => { // resetFields初始化到第一次打开dialog时里面的form表单里的值，所以先渲染form表单，后改变值，这样resetFields后未空表单
        this.editMaterialForm.userId = userId
        this.editMaterialForm.materialId = materialId
        this.editMaterialForm.userName = userName
        this.editMaterialForm.materialName = materialName
        this.editMaterialForm.requiredNumber = requiredNumber
        this.editMaterialForm.ownedNumber = ownedNumber
      })
    },
    // 关闭修改用户材料需求弹窗
    closeEditMaterial: function (done) {
      this.$confirm('确认关闭吗？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$refs['editMaterialForm'].resetFields()
        done()
      }).catch(() => {})
    },
    // 修改用户材料需求
    editMaterial: function () { // id, required, owned, userId
      this.$refs['editMaterialForm'].validate((valid) => {
        if (valid) {
          this.isLoading = true
          this.axios.post('/api/material/updateRequirement', this.editMaterialForm).then(res => {
            console.log('修改用户材料需求', res)
            this.$message({
              type: 'success',
              message: '修改成功'
            })
            this.$refs['editMaterialForm'].resetFields()
            this.editMaterialFormVisible = false
            this.search(this.searchName)
            this.isLoading = false
          }).catch(err => {
            console.log('修改用户材料需求出错', err)
            this.isLoading = false
          })
        } else {
          this.$message({
            type: 'error',
            message: '提交格式错误'
          })
        }
      })
      // this.isLoading = true
      // this.axios.post('/api/material/updateRequirement', {materialId: id, requiredNumber: required, ownedNumber: owned, userId: userId}).then(res => {
      //   console.log('修改用户材料需求', res)
      //   this.$message({
      //     type: 'success',
      //     message: '修改成功'
      //   })
      //   this.search(this.searchName)
      //   this.isLoading = false
      // }).catch(err => {
      //   console.log('修改用户材料需求出错', err)
      //   this.isLoading = false
      // })
    }
  }
}
</script>

<style scoped>
</style>
